<script>
  import { onMount } from 'svelte';

  let data = [];
  let newObjectId = '';
  let newJsonPath = '';
  let newTopic = '';
  let newEntityId = '';
  let newAttributeName = '';
  let newDescription = '';
  let matchDatapoint = false;

  let currentlyEditing = null;
  let tempData = null;

  async function fetchData() {
    const response = await fetch('http://localhost:8000/data');
    const responseData = await response.json();
    data = responseData.map(datapoint => ({
      ...datapoint, isEditing: false,
    }));
  }

  async function addData() {
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

function editData(datapoint) {
  currentlyEditing = datapoint.object_id;
  tempData = { ...datapoint };
}

function cancelEditing(datapoint) {
  currentlyEditing = null;
  tempData = null;
}

  async function deleteData(object_id) {
    const response = await fetch(`http://localhost:8000/data/${object_id}`, {
      method: 'DELETE',
    });
    if (response.ok) {
      fetchData();
    }
  }

  onMount(fetchData);
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
        <td>{row.status || ''}</td>
        <td>
          {#if currentlyEditing === row.object_id}
            <!-- this needs to be an arrow function to prevent it from being called on render -->
            <!-- otherwise it would be called on render and the data would be updated immediately without the user clicking the button -->
            <button on:click={() => updateData(tempData)}>Save</button>
            <button on:click={cancelEditing}>Cancel</button>
          {:else}
            <!-- same reason as above -->
            <button on:click={() => editData(row)}>Match</button>
            <button on:click={() => deleteData(row.object_id)}>Delete</button>
          {/if}
      </tr>
    {/each}
  </tbody>
</table>
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

