import { writable } from "svelte/store";
import type { Datapoint, DatapointUpdate } from "../services/api";

export const data = writable<Datapoint[]>([]);
export const currentlyEditing = writable<string | null>(null);
export const tempData = writable<DatapointUpdate | null>(null);
export const newDatapoint = writable<Datapoint | null>(null);