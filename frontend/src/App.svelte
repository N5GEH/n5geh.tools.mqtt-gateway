<script lang="ts">
  // Quick svelte rundown:
  // The code in the script tag is written in svelte, which is a javascript framework that compiles to vanilla javascript
  // Each component has a script tag, a body tag and a style tag
  // The script tag contains the javascript code for the component and is executed when the component is mounted
  // On the frontend, the code in the script tag is executed first, then the html code in the body tag is rendered and then the css code in the style tag is applied
  // The html code for the component is in the body tag
  // The style tag contains the css code for the component
  // Learn more about svelte here: https://svelte.dev/tutorial/basics
  import { onMount } from 'svelte';
  import dotenv from 'dotenv';

  import Status from './Status.svelte';
  import DataTable from './DataTable.svelte';
  import Form from './Form.svelte';
  dotenv.config();

  interface Datapoint {
    object_id: string;
    jsonpath: string;
    topic: string;
    description: string;
    entity_id: string;
    entity_type: string;
    attribute_name: string;
    matchDatapoint: boolean;
    status?: string | boolean;
  }

  interface SystemStatus {
    orion: string;
    postgres: string;
    redis: string;
  }

  // Variables for the form to add a new datapoint to the database
  // The newObjectId is generated on data submission and is not editable
  let API_HOST: string = process.env.API_HOST || 'http://localhost:8000';
  let data: Datapoint[] = [];
  let newObjectId: string = '';
  let newJsonPath: string = '';
  let newTopic: string = '';
  let newEntityId: string = '';
  let newEntityType: string = '';
  let newAttributeName: string = '';
  let newDescription: string = '';
  let matchDatapoint: boolean = false;

  // Variables for editing a datapoint
  // currentlyEditing is the object_id of the datapoint that is currently being edited
  // tempData is a copy of the datapoint that is currently being edited and is used to store the new values
  // so that the user can cancel the edit and the original values are not lost
  let currentlyEditing: string = null;
  let tempData: any = null;

  async function addData(): Promise<void> {
    // Add a new datapoint to the database
    // The object_id is generated on submission and is not editable
    const response: Response = await fetch(`${API_HOST}/data`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        object_id: crypto.randomUUID(),
        jsonpath: newJsonPath,
        topic: newTopic,
        description : newDescription,
        entity_id: matchDatapoint ? newEntityId : null,
        entity_type: matchDatapoint ? newEntityType : null,
        attribute_name: matchDatapoint ? newAttributeName : null,
        matchDatapoint
      }),
    });
    if (response.ok) {
      // reset the form in case the input was successful
      fetchData();
      newObjectId = '';
      newJsonPath = '';
      newTopic = '';
      newEntityId = '';
      newEntityType = '';
      newAttributeName = '';
      newDescription = '';
      matchDatapoint = false;
    }
  }

  async function updateData(datapoint: Datapoint): Promise<void> {
  // Update a datapoint in the database
  // This is called when the user clicks the save button after editing a datapoint in the table
    const response: Response = await fetch(`${API_HOST}/data/${datapoint.object_id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ entity_id: datapoint.entity_id, entity_type: datapoint.entity_type, attribute_name: datapoint.attribute_name, description: datapoint.description }),
    });
    if (response.ok) {
      currentlyEditing = null;
      tempData = null;
      fetchData();
    }
}

async function getStatus(object_id: string): Promise<string | boolean> {
  // Get the status of a datapoint
  // This is called when the data is fetched from the backend and is used to populate the status column in the table
  // It reflects whether an attribute with the given entity_id and attribute_name exists in the Context Broker
  try {
    const response = await fetch(`${API_HOST}/data/${object_id}/status`);
    if (!response.ok) throw new Error('Error');
    const status = await response.json();
    return status;
  } catch (e) {
    return false;
  }
}

async function getSystemStatus(): Promise<SystemStatus> {
  // Get the status of the Context Broker, PostgreSQL and Redis
  // This is called when the page is loaded and is used to display the status of the services in the header
  try {  
    const orionResponse = await fetch(`${API_HOST}/system/orion/status`);
    if (!orionResponse.ok) throw new Error('Orion error');
    const orionStatus = await orionResponse.json();

    const postgresResponse = await fetch(`${API_HOST}/system/postgres/status`);
    if (!postgresResponse.ok) throw new Error('Postgres error');
    const postgresStatus = await postgresResponse.json();

    const redisResponse = await fetch(`${API_HOST}/system/redis/status`);
    if (!redisResponse.ok) throw new Error('Redis error');
    const redisStatus = await redisResponse.json();

    return {
      orion: orionStatus,
      postgres: postgresStatus,
      redis: redisStatus,
    };
  } catch (e) {
    return {
      orion: e.message.includes('Orion') ? 'ERROR' : 'OK',
      postgres: e.message.includes('Postgres') ? 'ERROR' : 'OK',
      redis: e.message.includes('Redis') ? 'ERROR' : 'OK',
    };
  }
}

function editData(datapoint: Datapoint): void {
  // This is called when the user clicks the edit button in the table
  // It sets the currentlyEditing variable to the object_id of the datapoint that is being edited and stores a copy of the datapoint in tempData
  currentlyEditing = datapoint.object_id;
  tempData = { ...datapoint };
}

function cancelEditing(): void {
  // This is called when the user clicks the cancel button after editing a datapoint in the table
  // It resets the currentlyEditing variable and the tempData variable and cancels the edit
  currentlyEditing = null;
  tempData = null;
}
  onMount(fetchData); // fetch the data when the component is mounted (i.e. when the page is loaded)
</script>

<body>
  <h1>IoT Gateway</h1>
  <Status />
  <DataTable />
  <Form />
</body>

<style>

  body {
    font-family: sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    
  }

  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 1em;
    border: 1px solid #ccc;
  }
  th {
    background-color: #E62332;
  }

  table > tbody > tr > td > button {
    cursor: pointer;
    background-color: #E62332;
    width: 100%;
    margin: 0.25em 0 0.25em 0;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 0.25em;
    margin: 2em 2em 0 2em;
  }

  form > label {
    font-weight: bold;
    align-self: flex-start;
  }

  form > input {
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 0.25em;
  }

  button {
    cursor: pointer;
    background-color: #E62332;
  }

  .content {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
  }

  .status {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin: 0;
  }

  .status > p {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0.25em 0 0.25em 0;
  }

  .matchDatapoint {
    font-weight: bold;
    align-items: center;
    display: flex;
    flex-direction: row;
  }
</style>

