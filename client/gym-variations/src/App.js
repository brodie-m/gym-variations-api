import React, {useEffect} from 'react'
import './App.css';

function App() {

  useEffect(() => {
    fetch('/api/plan/chest').then(response =>
      response.json().then(data=> 
      console.log(data)))
  },[])

  return (
    <div className="App">
      
    </div>
  );
}

export default App;