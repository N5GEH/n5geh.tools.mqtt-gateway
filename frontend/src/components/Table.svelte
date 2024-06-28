<script lang="ts">
  import { onMount } from "svelte";
  import { updateData, deleteData } from "../services/api";
  import { data, currentlyEditing, tempData } from "../stores/stores";
  import { refreshData } from "../services/dataService";

  import type { Datapoint, DatapointUpdate } from "../services/api";

  let localTempData: DatapointUpdate = {
    object_id: '',
    description: '',
    entity_id: '',
    entity_type: '',
    attribute_name: ''
  };

  function editData(datapoint: Datapoint): void {
    currentlyEditing.set(datapoint.object_id);
    localTempData = { ...datapoint }; // Make a copy of the datapoint for editing
    console.log('Editing data:', localTempData);
  }

  function cancelEditing(): void {
    currentlyEditing.set(null);
    localTempData = {
      object_id: '',
      description: '',
      entity_id: '',
      entity_type: '',
      attribute_name: ''
    }; // Reset localTempData
    console.log('Cancelled editing.');
  }

  async function handleDelete(object_id: string): Promise<void> {
    try {
      await deleteData(object_id);
      console.log('Deleted data with object_id:', object_id);
      await refreshData(); // Refresh the table
    } catch (e) {
      console.error("An error occurred while deleting the data:", e);
    }
  }

  async function handleUpdate(): Promise<void> {
    try {
      console.log('Updating data:', localTempData);
      await updateData(localTempData); // Use localTempData for update
      currentlyEditing.set(null); // Reset the currentlyEditing variable
      await refreshData(); // Refresh the table
    } catch (e) {
      console.error("An error occurred while updating the data:", e);
    }
  }

  onMount(() => {
    console.log('Component mounted, calling refreshData...');
    refreshData();
  });
</script>

<div class="content">
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>JsonPATH</th>
        <th>Topic</th>
        <th>Description</th>
        <th>Entity ID</th>
        <th>Entity Type</th>
        <th>Attribute Name</th>
        <th>Status</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {#each $data as row (row.object_id)}
        <tr>
          <td>{row.object_id}</td>
          <td>{row.jsonpath}</td>
          <td>{row.topic}</td>
          <td>
            {#if $currentlyEditing === row.object_id}
              <input bind:value={localTempData.description} />
            {:else}
              {row.description || ""}
            {/if}
          </td>
          <td>
            {#if $currentlyEditing === row.object_id}
              <input bind:value={localTempData.entity_id} />
            {:else}
              {row.entity_id || ""}
            {/if}
          </td>
          <td>
            {#if $currentlyEditing === row.object_id}
              <input bind:value={localTempData.entity_type} />
            {:else}
              {row.entity_type || ""}
            {/if}
          </td>
          <td>
            {#if $currentlyEditing === row.object_id}
              <input bind:value={localTempData.attribute_name} />
            {:else}
              {row.attribute_name || ""}
            {/if}
          </td>
          <td>{row.status ? "Match found" : "No match"}</td>
          <td>
            {#if $currentlyEditing === row.object_id}
              <button on:click={handleUpdate}>Save</button>
              <button on:click={cancelEditing}>Cancel</button>
            {:else}
              <button on:click={() => editData(row)}>Configure</button>
              <button on:click={() => handleDelete(row.object_id)}>Delete</button>
            {/if}
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
