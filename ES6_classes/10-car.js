// 10-car.js

export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string') {
      throw new TypeError('Brand must be a string');
    }
    if (typeof motor !== 'string') {
      throw new TypeError('Motor must be a string');
    }
    if (typeof color !== 'string') {
      throw new TypeError('Color must be a string');
    }

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Symbol.species ensures cloneCar uses the right constructor
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
