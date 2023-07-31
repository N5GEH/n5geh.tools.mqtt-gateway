<script lang="ts">
    </script>

<html>
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
                    <input bind:value={tempData.entity_type} />
                  {:else}
                    {row.entity_type || ''}
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
        </div></html>