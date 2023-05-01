<script>
  import { onMount } from 'svelte';

  let data = [];
  let newObjectId = '';
  let newJsonPath = '';
  let newTopic = '';

  async function fetchData() {
    const response = await fetch('http://localhost:8000/data');
    data = await response.json();
  }

  async function addData() {
    const response = await fetch('http://localhost:8000/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ object_id: crypto.randomUUID(), jsonpath: newJsonPath, topic: newTopic }),
    });
    if (response.ok) {
      fetchData();
      newObjectId = '';
      newJsonPath = '';
      newTopic = '';
    }
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
    </tr>
  </thead>
  <tbody>
    {#each data as row}
      <tr>
        <td>{row.object_id}</td>
        <td>{row.jsonpath}</td>
        <td>{row.topic}</td>
        <td><button on:click={() => deleteData(row.object_id)}>Delete</button></td>
      </tr>
    {/each}
  </tbody>
</table>
<form on:submit|preventDefault={addData}>
  <label for="jsonpath">JsonPATH</label>
  <input type="text" id="jsonpath" bind:value={newJsonPath} required />
  <label for="topic">Topic</label>
  <input type="text" id="topic" bind:value={newTopic} required />
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

</style>

