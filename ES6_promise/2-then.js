export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success', // Using single quotes for the string
      };
    })
    .catch(() => {
      console.log('Got a response from the API');
      throw new Error();
    });
}