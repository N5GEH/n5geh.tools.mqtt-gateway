<script>
  // Quick svelte rundown:
  // The code in the script tag is written in svelte, which is a javascript framework that compiles to vanilla javascript
  // Each component has a script tag, a body tag and a style tag
  // The script tag contains the javascript code for the component and is executed when the component is mounted
  // On the frontend, the code in the script tag is executed first, then the html code in the body tag is rendered and then the css code in the style tag is applied
  // The html code for the component is in the body tag
  // The style tag contains the css code for the component
  // Learn more about svelte here: https://svelte.dev/tutorial/basics
  import { onMount } from 'svelte';

  // Variables for the form to add a new datapoint to the database
  // The newObjectId is generated on data submission and is not editable
  let data = [];
  let newObjectId = '';
  let newJsonPath = '';
  let newTopic = '';
  let newEntityId = '';
  let newAttributeName = '';
  let newDescription = '';
  let matchDatapoint = false;

  // Variables for editing a datapoint
  // currentlyEditing is the object_id of the datapoint that is currently being edited
  // tempData is a copy of the datapoint that is currently being edited and is used to store the new values
  // so that the user can cancel the edit and the original values are not lost
  let currentlyEditing = null;
  let tempData = null;

  async function fetchData() {
    // Fetch the data from the backend and store it in the data variable for use in the template
    // The status of each datapoint is also fetched and stored in the status variable
    // The data is then used to populate the table in the template
    const response = await fetch('http://localhost:8000/data');
    const responseData = await response.json();
    // since the status is fetched asynchronously, we need to wait for all the promises to resolve
    // before we can use the data
    data = await Promise.all(responseData.map(async row => {
      row.status = await getStatus(row.object_id);
      return row;
    }));
  }

  async function addData() {
    // Add a new datapoint to the database
    // The object_id is generated on submission and is not editable
    const response = await fetch('http://localhost:8000/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        object_id: crypto.randomUUID(),
        jsonpath: newJsonPath,
        topic: newTopic,
        description : newDescription,
        entity_id: matchDatapoint ? newEntityId : null,
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
      newAttributeName = '';
      newDescription = '';
      matchDatapoint = false;
    }
  }

  async function updateData(datapoint) {
  // Update a datapoint in the database
  // This is called when the user clicks the save button after editing a datapoint in the table
    const response = await fetch(`http://localhost:8000/data/${datapoint.object_id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ entity_id: datapoint.entity_id, attribute_name: datapoint.attribute_name, description: datapoint.description }),
    });
    if (response.ok) {
      currentlyEditing = null;
      tempData = null;
      fetchData();
    }
}

async function deleteData(object_id) {
    // Delete a datapoint from the database
    const response = await fetch(`http://localhost:8000/data/${object_id}`, {
      method: 'DELETE',
    });
    if (response.ok) {
      fetchData();
    }
  }

async function getStatus(object_id) {
  // Get the status of a datapoint
  // This is called when the data is fetched from the backend and is used to populate the status column in the table
  // It reflects whether an attribute with the given entity_id and attribute_name exists in the Context Broker
  const response = await fetch(`http://localhost:8000/data/${object_id}/status/`)
  const isOnline = await response.json();
  return isOnline;
}


function editData(datapoint) {
  // This is called when the user clicks the edit button in the table
  // It sets the currentlyEditing variable to the object_id of the datapoint that is being edited and stores a copy of the datapoint in tempData
  currentlyEditing = datapoint.object_id;
  tempData = { ...datapoint };
}

function cancelEditing(datapoint) {
  // This is called when the user clicks the cancel button after editing a datapoint in the table
  // It resets the currentlyEditing variable and the tempData variable and cancels the edit
  currentlyEditing = null;
  tempData = null;
}


  onMount(fetchData); // fetch the data when the component is mounted (i.e. when the page is loaded)
</script>

<body>
  <h1>IoT Gateway</h1>
<div class="content">
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>JsonPATH</th>
      <th>Topic</th>
      <th>Description</th>
      <th>Entity ID</th>
      <th>Attribute Name</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <!-- 
      The table is populated with the data fetched from the backend 
    -->
    {#each data as row (row.object_id)}
      <tr>
        <td>{row.object_id}</td>
        <td>{row.jsonpath}</td>
        <td>{row.topic}</td>
        <td>
          {#if currentlyEditing === row.object_id}
            <input bind:value={tempData.description} />
          {:else}
            {row.description || ''}
          {/if}
        </td>
        <td>
          {#if currentlyEditing === row.object_id}
            <input bind:value={tempData.entity_id} />
          {:else}
            {row.entity_id || ''}
          {/if}
        </td>
        <td>
          {#if currentlyEditing === row.object_id}
            <input bind:value={tempData.attribute_name} />
          {:else}
            {row.attribute_name || ''}
          {/if}
        </td>
        <td>{row.status ? 'Match found' : 'No match'}</td>
        <td>
          {#if currentlyEditing === row.object_id}
            <!-- this needs to be an arrow function to prevent it from being called on render -->
            <!-- otherwise it would be called on render and the data would be updated immediately without the user clicking the button -->
            <button on:click={() => updateData(tempData)}>Save</button>
            <button on:click={cancelEditing}>Cancel</button>
          {:else}
            <!-- same reason as above -->
            <button on:click={() => editData(row)}>{row.status ? 'Reconfigure' : 'Configure'}</button>
            <button on:click={() => deleteData(row.object_id)}>Delete</button>
          {/if}
      </tr>
    {/each}
  </tbody>
</table>
<!-- 
  The form is used to add new datapoints to the database
  preventDefault is used to prevent the page from reloading when the form is submitted
  so that the data can be added to the database without the page reloading which would cause the data to be lost
-->
<form on:submit|preventDefault={addData}>
  <label for="jsonpath">JsonPATH</label>
  <input type="text" id="jsonpath" bind:value={newJsonPath} required />
  <label for="topic">Topic</label>
  <input type="text" id="topic" bind:value={newTopic} required />
  <label for="description">Description</label>
  <input type="text" id="description" bind:value={newDescription}/>
  <div class="matchDatapoint">
    <label for="matchDatapoint">Match Datapoint</label>
    <input type="checkbox" id="matchDatapoint" bind:checked={matchDatapoint} />
  </div>
  {#if matchDatapoint}
    <label for="entity_id">Entity ID</label>
    <input type="text" id="entity_id" bind:value={newEntityId} required />
    <label for="attribute_name">Attribute Name</label>
    <input type="text" id="attribute_name" bind:value={newAttributeName} required />
  {/if}
  <button type="submit">Add Datapoint</button>
</form>
</div>
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

  .matchDatapoint {
    font-weight: bold;
    align-items: center;
    display: flex;
    flex-direction: row;
  }
</style>

