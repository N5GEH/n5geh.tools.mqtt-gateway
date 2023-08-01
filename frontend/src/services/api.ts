// contain all the api calls to the backend
let API_HOST = process.env.API_HOST || 'http://localhost:8000';

export interface Datapoint {
    object_id: string;
    jsonpath: string;
    topic: string;
    description: string;
    entity_id: string;
    entity_type: string;
    attribute_name: string;
    matchDatapoint: boolean;
    status?: string | boolean | undefined;
}

export interface DatapointUpdate {
    object_id: string;
    entity_id?: string | undefined;
    entity_type?: string | undefined;
    attribute_name?: string | undefined;
    description?: string | undefined;
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
    const responseData = await response.json();
    return responseData;
}

export const deleteData = async (object_id: string) => {
    const response: Response = await fetch(`${API_HOST}/data/${object_id}`, {
        method: 'DELETE',
    });
    const responseData = await response.json();
    return responseData;
}

export const getStatus = async (object_id: string) => {
    const response: Response = await fetch(`${API_HOST}/data/${object_id}status`);
    const responseData = await response.json();
    return responseData;
}

export const getSystemStatus = async (): Promise<SystemStatus> => {
    const response: Response = await fetch(`${API_HOST}/status`);
    const responseData = await response.json();
    return responseData;
}