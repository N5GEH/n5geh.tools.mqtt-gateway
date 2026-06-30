<!-- Form.svelte -->
<script lang="ts">
  import { run, preventDefault } from 'svelte/legacy';

  import { newDatapoint } from '../stores/stores';
  import type { Datapoint } from '../services/api';
  import { addData } from '../services/api';
  import { refreshData } from '../services/dataService';

  let formState: Partial<Datapoint> = $state({
    object_id: undefined,
    jsonpath: '',
    topic: '',
    description: '',
    entity_id: undefined,
    entity_type: undefined,
    attribute_name: undefined,
    connected: false,
    fiware_service: '',
  });

  let isMultiTenancy = $state(false); // New state for multi-tenancy checkbox

  // Reactive statement that updates whenever formState changes
  run(() => {
    newDatapoint.set(formState as Datapoint);
  });

  const handleSubmit = async (event: Event) => {
    event.preventDefault();
    // Build payload directly from formState to avoid race condition with run()
    const payload: Datapoint = {
      object_id: formState.object_id || undefined,
      jsonpath: formState.jsonpath || '',
      topic: formState.topic || '',
      description: formState.description || '',
      entity_id: formState.entity_id ?? null,
      entity_type: formState.entity_type ?? null,
      attribute_name: formState.attribute_name ?? null,
      connected: formState.connected ?? false,
      fiware_service: isMultiTenancy ? (formState.fiware_service || '') : undefined,
    };
    try {
      await addData(payload);
      await refreshData();
      formState = {
        object_id: undefined,
        jsonpath: '',
        topic: '',
        description: '',
        entity_id: undefined,
        entity_type: undefined,
        attribute_name: undefined,
        connected: false,
        fiware_service: '',
      };
      isMultiTenancy = false;
    } catch (e) {
      console.error('An error occurred while adding the data:', e);
    }
  };

</script>

<form onsubmit={preventDefault(handleSubmit)}>
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

  <!-- Multi-Tenancy Checkbox -->
  <div class="multi-tenancy">
    <label for="multiTenancy">Multi Tenancy</label>
    <input type="checkbox" id="multiTenancy" bind:checked={isMultiTenancy} />
  </div>
  
  {#if isMultiTenancy}
    <label for="fiware_service">FIWARE Service</label>
    <input type="text" id="fiware_service" bind:value={formState.fiware_service} required />
  {/if}

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
