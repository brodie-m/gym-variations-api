import React, {useEffect, useState} from 'react'
import './App.css';
import CustomNav from './components/CustomNav';
import Plan from './components/Plan';
import PlanMenu from './components/PlanMenu';

function App() {

  const [plan, setPlan] = useState([])
  const [group, setGroup] = useState('')
  useEffect(() => {
    const options = {
      'method': 'POST',
      'headers': {
        'Content-Type': 'application/json'
      },
      'body': {
        group
      }
    }
    fetch('/api/plan/ohp', options).then(response =>
      response.json().then(data=> 
      setPlan(data)))
  },[group])

  return (
    <div className="App">
      <CustomNav/>
      <PlanMenu/>
      {plan && <Plan plan={plan}/>}
    </div>
  );
}

export default App;
