import React from 'react'
import { Button, Container, Form } from 'react-bootstrap'

export default function PlanMenu() {
    return (
        <Container>
            <Form className = 'p-2 m-2'>
                <Form.Group>
                    <Form.Label>
                        Main exercise
                    </Form.Label>
                    <Form.Select>
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
                    <Form.Control type='number' placeholder='no judgement'>
                        
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
    )
}
