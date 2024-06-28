// dataservice.ts
import { data } from '../stores/stores';
import { fetchData } from './api';

export async function refreshData(): Promise<void> {
  try {
    console.log('Calling refreshData...');
    const fetchedData = await fetchData();
    console.log('Fetched data:', fetchedData);
    data.set(fetchedData); // Update the data store with the fetched data
  } catch (e) {
    console.error('An error occurred while fetching the data:', e);
  }
}
