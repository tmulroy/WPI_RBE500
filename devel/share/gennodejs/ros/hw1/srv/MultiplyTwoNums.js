// Auto-generated. Do not edit!

// (in-package hw1.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class MultiplyTwoNumsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
      this.b = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = 0.0;
      }
      if (initObj.hasOwnProperty('b')) {
        this.b = initObj.b
      }
      else {
        this.b = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MultiplyTwoNumsRequest
    // Serialize message field [a]
    bufferOffset = _serializer.float64(obj.a, buffer, bufferOffset);
    // Serialize message field [b]
    bufferOffset = _serializer.float64(obj.b, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MultiplyTwoNumsRequest
    let len;
    let data = new MultiplyTwoNumsRequest(null);
    // Deserialize message field [a]
    data.a = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [b]
    data.b = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'hw1/MultiplyTwoNumsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6f4f9f1b571de73ae8592a1438fd23f3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 a
    float64 b
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MultiplyTwoNumsRequest(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = 0.0
    }

    if (msg.b !== undefined) {
      resolved.b = msg.b;
    }
    else {
      resolved.b = 0.0
    }

    return resolved;
    }
};

class MultiplyTwoNumsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.product = null;
    }
    else {
      if (initObj.hasOwnProperty('product')) {
        this.product = initObj.product
      }
      else {
        this.product = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MultiplyTwoNumsResponse
    // Serialize message field [product]
    bufferOffset = _serializer.float64(obj.product, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MultiplyTwoNumsResponse
    let len;
    let data = new MultiplyTwoNumsResponse(null);
    // Deserialize message field [product]
    data.product = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'hw1/MultiplyTwoNumsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99cd9447c43db28d0ace52a5a30ce74f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    float64 product
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MultiplyTwoNumsResponse(null);
    if (msg.product !== undefined) {
      resolved.product = msg.product;
    }
    else {
      resolved.product = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: MultiplyTwoNumsRequest,
  Response: MultiplyTwoNumsResponse,
  md5sum() { return 'fa76f5fbe76a971f9b1d5d312793b2e8'; },
  datatype() { return 'hw1/MultiplyTwoNums'; }
};
