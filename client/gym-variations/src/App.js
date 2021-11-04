import React, {useEffect, useState} from 'react'
import { Container, Form, Button } from 'react-bootstrap';
import './App.css';
import CustomNav from './components/CustomNav';
import Plan from './components/Plan';
import PlanMenu from './components/PlanMenu';

function App() {
  const [plan, setPlan] = useState([])
  const [group, setGroup] = useState('')
  const [oneRepMax, setOneRepMax] = useState(0)
  console.log(group,oneRepMax)
  async function handleSubmit(e) {
    try {
      e.preventDefault();
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "group":group,
        "oneRepMax":oneRepMax
      })
    }
    const result = await fetch(`/api/plan/${group}`,options)
    const data = await result.json()
    setPlan(data)
  }
    catch(error) {
      console.log(error)
    }
    
  }

  


  return (
    <div className="App">
      <CustomNav/>
      <Container>
            <Form className = 'p-2 m-2' onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label>
                        Main exercise
                    </Form.Label>
                    <Form.Select onChange={(e) => setGroup(e.target.value)}>
                        <option>bench</option>
                        <option>squat</option>
                        <option>diddy</option>
                        <option>ohp</option>
                    </Form.Select>
                    <Form.Text>
                        which exercise are you hitting today?
                    </Form.Text>
                </Form.Group>
                    <br/>
                    <br/>
                    <Form.Group>

                    <Form.Label>
                        One rep max
                    </Form.Label>
                    <Form.Control type='number' placeholder='no judgement' onChange={(e) => setOneRepMax(e.target.value)}>
                        
                    </Form.Control>
                    <Form.Text>
                        enter your one rep max in kg
                    </Form.Text>
                    </Form.Group>
                    
                <Button variant='primary' type='submit'>
                    submit
                </Button>
            </Form>
        </Container>
      {plan && <Plan plan={plan}/>}
    </div>
  );
}

export default App;
