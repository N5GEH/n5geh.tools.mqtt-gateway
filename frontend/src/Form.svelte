<script lang="ts">
    </script>

<html>
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
          <label for="entity_type">Entity Type</label>
          <input type="text" id="entity_type" bind:value={newEntityType} required />
          <label for="attribute_name">Attribute Name</label>
          <input type="text" id="attribute_name" bind:value={newAttributeName} required />
        {/if}
        <button type="submit">Add Datapoint</button>
      </form>
</html>