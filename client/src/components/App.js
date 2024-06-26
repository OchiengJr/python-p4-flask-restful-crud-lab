import React from "react";
import Header from "./Header";
import PlantPage from "./PlantPage";
// Import ErrorBoundary if needed

function App() {
  // Add state and state management hooks if necessary
  
  return (
    <div className="app">
      <Header />
      <PlantPage />
      {/* Add ErrorBoundary components if needed */}
    </div>
  );
}

export default App;
