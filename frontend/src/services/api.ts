// contain all the api calls to the backend
// let API_HOST = process.env.API_HOST || 'http://localhost:8000';
const API_HOST: string = process.env.API_HOST || "http://api:8000";

export interface Datapoint {
    object_id?: string;
    jsonpath: string;
    topic: string;
    description: string;
    entity_id: string | null; // Can be a string or null
    entity_type: string | null; // Can be a string or null
    attribute_name: string | null; // Can be a string or null
    matchDatapoint: boolean;
    status?: string | boolean | null; // Can be a string, boolean, or null
}

export interface DatapointUpdate {
    object_id: string;
    entity_id?: string;
    entity_type?: string;
    attribute_name?: string;
    description?: string;
}

export interface SystemStatus {
    orion: boolean;
    postgres: boolean;
    redis: boolean;
}


export const fetchData = async (): Promise<Datapoint[]> => {
    const response: Response = await fetch(`${API_HOST}/data`);
    const responseData = await response.json();
    let data: Datapoint[] = await Promise.all(responseData.map(async row => {
        row.status = await getStatus(row.object_id);
        return row;
      }));
    return data;
};

export const addData = async (data: Datapoint) => {
    const response: Response = await fetch(`${API_HOST}/data`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    const responseData = await response.json();
    return responseData;
}

export const updateData = async (data: DatapointUpdate) => {
    const response: Response = await fetch(`${API_HOST}/data/${data.object_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        throw new Error(`Failed to update datapoint with object_id ${data.object_id}`);
    }
    const responseData = await response.json();
    return responseData;
}

export const deleteData = async (object_id: string): Promise<Datapoint | null> => {
    const response: Response = await fetch(`${API_HOST}/data/${object_id}`, {
        method: 'DELETE',
    });
    // the server returns a 204 No Content response if the delete was successful
    if (response.status === 204) {
        return null;
    } else if (!response.ok) {
        throw new Error(`Failed to delete datapoint with object_id ${object_id}`);
    }
    const responseData = await response.json();
    return responseData;
}

export const getStatus = async (object_id: string): Promise<string | boolean | null> => {
    const response: Response = await fetch(`${API_HOST}/data/${object_id}/status`);
    if (!response.ok) {
        throw new Error(`Failed to get status for datapoint with object_id ${object_id}`);
    }
    const responseData = await response.json();
    return responseData.status;
}

export const getSystemStatus = async (): Promise<SystemStatus> => {
    const response: Response = await fetch(`${API_HOST}/system/status`);
    if (!response.ok) {
        throw new Error(`Failed to get system status`);
    }
    const responseData = await response.json();
    return responseData;
}