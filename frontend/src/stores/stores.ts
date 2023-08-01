import { writable } from "svelte/store";

interface Datapoint {
    object_id: string;
    jsonpath: string;
    topic: string;
    description: string;
    entity_id: string;
    entity_type: string;
    attribute_name: string;
    matchDatapoint: boolean;
    status?: string | boolean;
}

interface DatapointUpdate {
    object_id: string;
    entity_id?: string;
    entity_type?: string;
    attribute_name?: string;
    description?: string;
}

export const data = writable<Datapoint[]>([]);
export const currentlyEditing = writable<string | null>(null);
export const tempData = writable<Datapoint | null>(null);
export const newDatapoint = writable<Datapoint | null>(null);