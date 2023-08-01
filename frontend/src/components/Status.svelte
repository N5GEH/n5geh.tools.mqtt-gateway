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
            <p class="status-ok">Orion: {systemStatus.orion}</p>
            <p class="status-ok">Postgres: {systemStatus.postgres}</p>
            <p class="status-ok">Redis: {systemStatus.redis}</p>
        {:else}
            <p class="status-error">Checking...</p>
        {/if}
    </div>
</html>
      