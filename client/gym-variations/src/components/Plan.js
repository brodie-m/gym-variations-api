import React from 'react'
import {List, Header} from 'semantic-ui-react'
export default function Plan({plan}) {
    return (
        <List className = 'p-2 m-2'>
            {plan.map(exercise => {
                return (
                    <List.Item key={exercise.name}>
                        <Header>{exercise.name}</Header>
                        Sets: {exercise.sets}, Reps: {exercise.reps}, Weight: {exercise.weight}
                        
                    </List.Item>
                )
            })}
        </List>
    )
}
