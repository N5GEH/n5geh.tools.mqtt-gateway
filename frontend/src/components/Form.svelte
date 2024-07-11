<script lang='ts'>
  import { newDatapoint, data } from '../stores/stores'; // Import the data store
  import type { Datapoint } from '../services/api';
  import { addData } from '../services/api';
  import { refreshData } from '../services/dataService';

  let formState: Partial<Datapoint> = {
    object_id: null,
    jsonpath: '',
    topic: '',
    description: '',
    entity_id: null,
    entity_type: null,
    attribute_name: null,
    connected: false
  };

  // Reactive statement that updates whenever formState changes
  $: newDatapoint.set(formState as Datapoint);

  const handleSubmit = async (event: Event) => {
    event.preventDefault();
    try {
      await addData($newDatapoint);
      await refreshData(); // Refresh the data after adding a new datapoint
      // Reset formState after successful addition
      formState = {
        object_id: null,
        jsonpath: '',
        topic: '',
        description: '',
        entity_id: null,
        entity_type: null,
        attribute_name: null,
        connected: false
      };
    } catch (e) {
      console.error('An error occurred while adding the data:', e);
    }
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <!-- Input field for object_id -->
  <label for="object_id">Object ID</label>
  <input type="text" id="object_id" bind:value={formState.object_id} />

  <!-- Bind each input field to the corresponding property in formState -->
  <label for="jsonpath">JsonPATH</label>
  <input type="text" id="jsonpath" bind:value={formState.jsonpath} required />
  <label for="topic">Topic</label>
  <input type="text" id="topic" bind:value={formState.topic} required />
  <label for="description">Description</label>
  <input type="text" id="description" bind:value={formState.description} />
  <div class="connected">
    <label for="connected">Match Datapoint</label>
    <input type="checkbox" id="connected" bind:checked={formState.connected} />
  </div>
  {#if formState.connected}
    <label for="entity_id">Entity ID</label>
    <input
      type="text"
      id="entity_id"
      bind:value={formState.entity_id}
      required
    />
    <label for="entity_type">Entity Type</label>
    <input
      type="text"
      id="entity_type"
      bind:value={formState.entity_type}
      required
    />
    <label for="attribute_name">Attribute Name</label>
    <input
      type="text"
      id="attribute_name"
      bind:value={formState.attribute_name}
      required
    />
  {/if}
  <button type="submit">Add Datapoint</button>
</form>
