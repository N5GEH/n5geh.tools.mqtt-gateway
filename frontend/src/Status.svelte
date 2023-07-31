<script lang="ts">
    // component for displaying the status of the services
    interface SystemStatus {
        orion: string;
        postgres: string;
        redis: string;
    }


    async function getSystemStatus(): Promise<SystemStatus> {
        const res = await fetch(`${process.env.API_HOST}/status`);
        if (res.ok) {
            return await res.json();
        } else {
            throw new Error(`Error fetching system status: ${res.statusText}`);
        }
        
    }


</script>

<html>
    <div class="status">
        <p>Services status:</p>
        {#await getSystemStatus()}
            <p>Checking...</p>
        {:then systemStatus}
            <p>Orion: {systemStatus.orion}</p>
            <p>PostgreSQL: {systemStatus.postgres}</p>
            <p>Redis: {systemStatus.redis}</p>
        {:catch error}
          <p>Error: {error.message}</p>
        {/await}
    </div>
</html>
      