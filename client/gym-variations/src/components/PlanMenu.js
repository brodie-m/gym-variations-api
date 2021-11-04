import React from 'react'
import { Container, Form } from 'react-bootstrap'

export default function PlanMenu() {
    return (
        <Container>
            <Form>
                <Form.Group>
                    <Form.Label>
                        Group
                    </Form.Label>
                    <Form.Select>
                        <option>chest</option>
                        <option>squat</option>
                        <option>diddy</option>
                        <option>ohp</option>
                    </Form.Select>
                    <Form.Text>
                        which group are you hitting today?
                    </Form.Text>
                </Form.Group>
            </Form>
        </Container>
    )
}
