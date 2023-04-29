<script>
  import { onMount } from 'svelte';

  let data = [];

  onMount(async () => {
    const response = await fetch('http://localhost:8000/data');
    data = await response.json();
  });
</script>

<body>
  <h1>IoT Gateway</h1>
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
      </tr>
    {/each}
  </tbody>
</table>
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
    background-color: #f3f3f3;
  }
</style>

