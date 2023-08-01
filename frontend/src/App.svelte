<script lang="ts">
  import Status from './components/Status.svelte';
  import Table from './components/Table.svelte';
  import Form from './components/Form.svelte';
</script>

<body>
  <h1>IoT Gateway</h1>
  <Status />
  <Table />
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

