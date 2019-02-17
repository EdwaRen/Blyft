import React from 'react';

import {
  Button,
  Form,
  Grid,
  Header,
  Message,
  Segment,
} from 'semantic-ui-react';

export default () => (
  <Grid centered columns={2}>
    <Grid.Column>
      <Header as="h2" textAlign="center">
        BusPool
      </Header>
      <Segment>
        <Form size="large">
          <Form.Input
            fluid
            icon="location arrow"
            iconPosition="left"
            placeholder="Address of start point"
          />
          <Form.Input
            fluid
            icon="location arrow"
            iconPosition="left"
            placeholder="Address of end point"
          />
          <Button color="blue" fluid size="large">
            Enter the start and end point of your trip
          </Button>
        </Form>
      </Segment>
    </Grid.Column>
  </Grid>
);
