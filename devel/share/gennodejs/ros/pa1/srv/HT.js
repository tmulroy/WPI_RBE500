// Auto-generated. Do not edit!

// (in-package pa1.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class HTRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ht11 = null;
      this.ht12 = null;
      this.ht13 = null;
      this.ht14 = null;
      this.ht21 = null;
      this.ht22 = null;
      this.ht23 = null;
      this.ht24 = null;
      this.ht31 = null;
      this.ht32 = null;
      this.ht33 = null;
      this.ht34 = null;
      this.ht41 = null;
      this.ht42 = null;
      this.ht43 = null;
      this.ht44 = null;
    }
    else {
      if (initObj.hasOwnProperty('ht11')) {
        this.ht11 = initObj.ht11
      }
      else {
        this.ht11 = 0.0;
      }
      if (initObj.hasOwnProperty('ht12')) {
        this.ht12 = initObj.ht12
      }
      else {
        this.ht12 = 0.0;
      }
      if (initObj.hasOwnProperty('ht13')) {
        this.ht13 = initObj.ht13
      }
      else {
        this.ht13 = 0.0;
      }
      if (initObj.hasOwnProperty('ht14')) {
        this.ht14 = initObj.ht14
      }
      else {
        this.ht14 = 0.0;
      }
      if (initObj.hasOwnProperty('ht21')) {
        this.ht21 = initObj.ht21
      }
      else {
        this.ht21 = 0.0;
      }
      if (initObj.hasOwnProperty('ht22')) {
        this.ht22 = initObj.ht22
      }
      else {
        this.ht22 = 0.0;
      }
      if (initObj.hasOwnProperty('ht23')) {
        this.ht23 = initObj.ht23
      }
      else {
        this.ht23 = 0.0;
      }
      if (initObj.hasOwnProperty('ht24')) {
        this.ht24 = initObj.ht24
      }
      else {
        this.ht24 = 0.0;
      }
      if (initObj.hasOwnProperty('ht31')) {
        this.ht31 = initObj.ht31
      }
      else {
        this.ht31 = 0.0;
      }
      if (initObj.hasOwnProperty('ht32')) {
        this.ht32 = initObj.ht32
      }
      else {
        this.ht32 = 0.0;
      }
      if (initObj.hasOwnProperty('ht33')) {
        this.ht33 = initObj.ht33
      }
      else {
        this.ht33 = 0.0;
      }
      if (initObj.hasOwnProperty('ht34')) {
        this.ht34 = initObj.ht34
      }
      else {
        this.ht34 = 0.0;
      }
      if (initObj.hasOwnProperty('ht41')) {
        this.ht41 = initObj.ht41
      }
      else {
        this.ht41 = 0.0;
      }
      if (initObj.hasOwnProperty('ht42')) {
        this.ht42 = initObj.ht42
      }
      else {
        this.ht42 = 0.0;
      }
      if (initObj.hasOwnProperty('ht43')) {
        this.ht43 = initObj.ht43
      }
      else {
        this.ht43 = 0.0;
      }
      if (initObj.hasOwnProperty('ht44')) {
        this.ht44 = initObj.ht44
      }
      else {
        this.ht44 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HTRequest
    // Serialize message field [ht11]
    bufferOffset = _serializer.float64(obj.ht11, buffer, bufferOffset);
    // Serialize message field [ht12]
    bufferOffset = _serializer.float64(obj.ht12, buffer, bufferOffset);
    // Serialize message field [ht13]
    bufferOffset = _serializer.float64(obj.ht13, buffer, bufferOffset);
    // Serialize message field [ht14]
    bufferOffset = _serializer.float64(obj.ht14, buffer, bufferOffset);
    // Serialize message field [ht21]
    bufferOffset = _serializer.float64(obj.ht21, buffer, bufferOffset);
    // Serialize message field [ht22]
    bufferOffset = _serializer.float64(obj.ht22, buffer, bufferOffset);
    // Serialize message field [ht23]
    bufferOffset = _serializer.float64(obj.ht23, buffer, bufferOffset);
    // Serialize message field [ht24]
    bufferOffset = _serializer.float64(obj.ht24, buffer, bufferOffset);
    // Serialize message field [ht31]
    bufferOffset = _serializer.float64(obj.ht31, buffer, bufferOffset);
    // Serialize message field [ht32]
    bufferOffset = _serializer.float64(obj.ht32, buffer, bufferOffset);
    // Serialize message field [ht33]
    bufferOffset = _serializer.float64(obj.ht33, buffer, bufferOffset);
    // Serialize message field [ht34]
    bufferOffset = _serializer.float64(obj.ht34, buffer, bufferOffset);
    // Serialize message field [ht41]
    bufferOffset = _serializer.float64(obj.ht41, buffer, bufferOffset);
    // Serialize message field [ht42]
    bufferOffset = _serializer.float64(obj.ht42, buffer, bufferOffset);
    // Serialize message field [ht43]
    bufferOffset = _serializer.float64(obj.ht43, buffer, bufferOffset);
    // Serialize message field [ht44]
    bufferOffset = _serializer.float64(obj.ht44, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HTRequest
    let len;
    let data = new HTRequest(null);
    // Deserialize message field [ht11]
    data.ht11 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht12]
    data.ht12 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht13]
    data.ht13 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht14]
    data.ht14 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht21]
    data.ht21 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht22]
    data.ht22 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht23]
    data.ht23 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht24]
    data.ht24 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht31]
    data.ht31 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht32]
    data.ht32 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht33]
    data.ht33 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht34]
    data.ht34 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht41]
    data.ht41 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht42]
    data.ht42 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht43]
    data.ht43 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ht44]
    data.ht44 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 128;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pa1/HTRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b73c7247aab620f8f17139f7c17d037f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 ht11
    float64 ht12
    float64 ht13
    float64 ht14
    float64 ht21
    float64 ht22
    float64 ht23
    float64 ht24
    float64 ht31
    float64 ht32
    float64 ht33
    float64 ht34
    float64 ht41
    float64 ht42
    float64 ht43
    float64 ht44
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HTRequest(null);
    if (msg.ht11 !== undefined) {
      resolved.ht11 = msg.ht11;
    }
    else {
      resolved.ht11 = 0.0
    }

    if (msg.ht12 !== undefined) {
      resolved.ht12 = msg.ht12;
    }
    else {
      resolved.ht12 = 0.0
    }

    if (msg.ht13 !== undefined) {
      resolved.ht13 = msg.ht13;
    }
    else {
      resolved.ht13 = 0.0
    }

    if (msg.ht14 !== undefined) {
      resolved.ht14 = msg.ht14;
    }
    else {
      resolved.ht14 = 0.0
    }

    if (msg.ht21 !== undefined) {
      resolved.ht21 = msg.ht21;
    }
    else {
      resolved.ht21 = 0.0
    }

    if (msg.ht22 !== undefined) {
      resolved.ht22 = msg.ht22;
    }
    else {
      resolved.ht22 = 0.0
    }

    if (msg.ht23 !== undefined) {
      resolved.ht23 = msg.ht23;
    }
    else {
      resolved.ht23 = 0.0
    }

    if (msg.ht24 !== undefined) {
      resolved.ht24 = msg.ht24;
    }
    else {
      resolved.ht24 = 0.0
    }

    if (msg.ht31 !== undefined) {
      resolved.ht31 = msg.ht31;
    }
    else {
      resolved.ht31 = 0.0
    }

    if (msg.ht32 !== undefined) {
      resolved.ht32 = msg.ht32;
    }
    else {
      resolved.ht32 = 0.0
    }

    if (msg.ht33 !== undefined) {
      resolved.ht33 = msg.ht33;
    }
    else {
      resolved.ht33 = 0.0
    }

    if (msg.ht34 !== undefined) {
      resolved.ht34 = msg.ht34;
    }
    else {
      resolved.ht34 = 0.0
    }

    if (msg.ht41 !== undefined) {
      resolved.ht41 = msg.ht41;
    }
    else {
      resolved.ht41 = 0.0
    }

    if (msg.ht42 !== undefined) {
      resolved.ht42 = msg.ht42;
    }
    else {
      resolved.ht42 = 0.0
    }

    if (msg.ht43 !== undefined) {
      resolved.ht43 = msg.ht43;
    }
    else {
      resolved.ht43 = 0.0
    }

    if (msg.ht44 !== undefined) {
      resolved.ht44 = msg.ht44;
    }
    else {
      resolved.ht44 = 0.0
    }

    return resolved;
    }
};

class HTResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.q1 = null;
      this.q2 = null;
      this.d3 = null;
    }
    else {
      if (initObj.hasOwnProperty('q1')) {
        this.q1 = initObj.q1
      }
      else {
        this.q1 = 0.0;
      }
      if (initObj.hasOwnProperty('q2')) {
        this.q2 = initObj.q2
      }
      else {
        this.q2 = 0.0;
      }
      if (initObj.hasOwnProperty('d3')) {
        this.d3 = initObj.d3
      }
      else {
        this.d3 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HTResponse
    // Serialize message field [q1]
    bufferOffset = _serializer.float64(obj.q1, buffer, bufferOffset);
    // Serialize message field [q2]
    bufferOffset = _serializer.float64(obj.q2, buffer, bufferOffset);
    // Serialize message field [d3]
    bufferOffset = _serializer.float64(obj.d3, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HTResponse
    let len;
    let data = new HTResponse(null);
    // Deserialize message field [q1]
    data.q1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q2]
    data.q2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [d3]
    data.d3 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pa1/HTResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f439218c3a6a6da84daea3b1bccc8aa6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 q1
    float64 q2
    float64 d3
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HTResponse(null);
    if (msg.q1 !== undefined) {
      resolved.q1 = msg.q1;
    }
    else {
      resolved.q1 = 0.0
    }

    if (msg.q2 !== undefined) {
      resolved.q2 = msg.q2;
    }
    else {
      resolved.q2 = 0.0
    }

    if (msg.d3 !== undefined) {
      resolved.d3 = msg.d3;
    }
    else {
      resolved.d3 = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: HTRequest,
  Response: HTResponse,
  md5sum() { return '41bf0543de79fcb6f767b6c9848b88ec'; },
  datatype() { return 'pa1/HT'; }
};
