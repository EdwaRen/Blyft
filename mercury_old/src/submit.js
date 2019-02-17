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
            placeholder="Email address"
          />
          <Form.Input
            fluid
            icon="location arrow"
            iconPosition="left"
            placeholder="Password"
            type="password"
          />

          <Button color="blue" fluid size="large">
            Enter Latitude and Longitude
          </Button>
        </Form>
      </Segment>
      <Message>
        Not registered yet? <a href="#">Sign Up</a>
      </Message>
    </Grid.Column>
  </Grid>
);
