<script lang="ts">
    import { getSystemStatus } from '../services/api';
    import { onMount } from 'svelte';

    import type { SystemStatus } from '../services/api';

    let systemStatus: SystemStatus;

    onMount(async () => {
        try {
            systemStatus = await getSystemStatus();
        } catch (e) {
            console.error(e);
        }
    });
</script>


<html lang="en">
    <div class="status">
        <p>Services status:</p>
        {#if systemStatus}
            <p class="status-ok"><span class="circle" style="background-color:{systemStatus.orion.status ? 'green' : 'red'}"></span>Orion</p>
            <p class="status-ok"><span class="circle" style="background-color:{systemStatus.postgres.status ? 'green' : 'red'}"></span>Postgres</p>
            <p class="status-ok"><span class="circle" style="background-color:{systemStatus.redis.status ? 'green' : 'red'}"></span>Redis</p>
        {:else}
            <p class="status-error">Checking...</p>
        {/if}
    </div>
</html>
      
