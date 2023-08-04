import { data } from '../stores/stores';
import { fetchData } from './api';

export async function refreshData(): Promise<void> {
  try {
    data.set(await fetchData());
  } catch (e) {
    console.error('An error occurred while fetching the data:', e);
  }
}