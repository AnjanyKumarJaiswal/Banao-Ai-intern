import { useState } from "react";

function App() {
  const [query, setQuery] = useState(""); // Store user input
  const [response, setResponse] = useState(null); // Store backend response
  const [loading, setLoading] = useState(false); // Loading state

  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent page reload
    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch(`http://localhost:8000/execute?query=${encodeURIComponent(query)}`);
      const data = await res.json();

      if (data.error) {
        setResponse({ error: data.error });
      } else {
        setResponse({ result: data.response });
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponse({ error: "There was an error processing your request." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
      <h1 className="text-4xl font-bold mb-8 text-center font-sans">Query Processor</h1>
      
      {/* Display the user's query */}
      {query && !loading && (
        <div className="bg-white shadow-lg rounded-md p-4 w-3/4 text-center mb-4 text-xl">
          <p className="text-gray-700 font-medium">Your Query: {query}</p>
        </div>
      )}

      {/* Display the backend response */}
      {response && !loading && (
        <div className={`bg-${response.error ? "red" : "blue"}-100 shadow-md rounded-md p-4 w-3/4 text-center mt-4 text-lg`}>
          <h3 className={`font-semibold text-${response.error ? "red" : "blue"}-800`}>
            {response.error ? "Error:" : "Response:"}
          </h3>
          <pre className="whitespace-pre-line text-gray-800">
            {response.error ? response.error : response.result}
          </pre>
        </div>
      )}

      {/* Show loading state */}
      {loading && <p className="text-lg mt-4 text-gray-600">Processing your request...</p>}

      {/* Form at the bottom center */}
      <form 
        onSubmit={handleSubmit} 
        className="fixed bottom-10 w-full max-w-3xl flex flex-col items-center"
      >
        <input
          type="text"
          placeholder="Enter your query here"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-3/4 p-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-400 text-lg"
        />
        <button
          type="submit"
          className="mt-4 bg-purple-500 text-white w-3/4 py-3 text-lg rounded-lg hover:bg-purple-600 transition"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default App;
