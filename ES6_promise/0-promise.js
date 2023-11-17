export default function getResponseFromAPI() {
  // Assuming some asynchronous operation, like fetching data from an API
  return new Promise((resolve) => {
    // Simulating a successful API response after 1 second
    setTimeout(() => {
      resolve('API response data');
    }, 1000);
  });
}
