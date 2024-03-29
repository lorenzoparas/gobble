/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const onCreateRestaurant = /* GraphQL */ `
  subscription OnCreateRestaurant(
    $filter: ModelSubscriptionRestaurantFilterInput
  ) {
    onCreateRestaurant(filter: $filter) {
      id
      name
      lat
      long
      createdAt
      updatedAt
      __typename
    }
  }
`;
export const onUpdateRestaurant = /* GraphQL */ `
  subscription OnUpdateRestaurant(
    $filter: ModelSubscriptionRestaurantFilterInput
  ) {
    onUpdateRestaurant(filter: $filter) {
      id
      name
      lat
      long
      createdAt
      updatedAt
      __typename
    }
  }
`;
export const onDeleteRestaurant = /* GraphQL */ `
  subscription OnDeleteRestaurant(
    $filter: ModelSubscriptionRestaurantFilterInput
  ) {
    onDeleteRestaurant(filter: $filter) {
      id
      name
      lat
      long
      createdAt
      updatedAt
      __typename
    }
  }
`;
export const onCreateMenuItem = /* GraphQL */ `
  subscription OnCreateMenuItem($filter: ModelSubscriptionMenuItemFilterInput) {
    onCreateMenuItem(filter: $filter) {
      id
      name
      price
      restaurantId
      createdAt
      updatedAt
      __typename
    }
  }
`;
export const onUpdateMenuItem = /* GraphQL */ `
  subscription OnUpdateMenuItem($filter: ModelSubscriptionMenuItemFilterInput) {
    onUpdateMenuItem(filter: $filter) {
      id
      name
      price
      restaurantId
      createdAt
      updatedAt
      __typename
    }
  }
`;
export const onDeleteMenuItem = /* GraphQL */ `
  subscription OnDeleteMenuItem($filter: ModelSubscriptionMenuItemFilterInput) {
    onDeleteMenuItem(filter: $filter) {
      id
      name
      price
      restaurantId
      createdAt
      updatedAt
      __typename
    }
  }
`;
