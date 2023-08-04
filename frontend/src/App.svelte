<script lang="ts">
  import Status from './components/Status.svelte';
  import Table from './components/Table.svelte';
  import Form from './components/Form.svelte';
</script>

<body>
  <h1>IoT Gateway</h1>
  <div class="status-container">
    <Status />
  </div>
  <div class="content-container">
    <div class="table-container"><Table /></div>
    <div class="form-container"><Form /></div>
  </div>
</body>
