// Auto-generated. Do not edit!

// (in-package fk.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class JointVariables {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.q1 = null;
      this.q2 = null;
      this.q3 = null;
      this.q4 = null;
      this.q5 = null;
      this.q6 = null;
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
      if (initObj.hasOwnProperty('q3')) {
        this.q3 = initObj.q3
      }
      else {
        this.q3 = 0.0;
      }
      if (initObj.hasOwnProperty('q4')) {
        this.q4 = initObj.q4
      }
      else {
        this.q4 = 0.0;
      }
      if (initObj.hasOwnProperty('q5')) {
        this.q5 = initObj.q5
      }
      else {
        this.q5 = 0.0;
      }
      if (initObj.hasOwnProperty('q6')) {
        this.q6 = initObj.q6
      }
      else {
        this.q6 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointVariables
    // Serialize message field [q1]
    bufferOffset = _serializer.float64(obj.q1, buffer, bufferOffset);
    // Serialize message field [q2]
    bufferOffset = _serializer.float64(obj.q2, buffer, bufferOffset);
    // Serialize message field [q3]
    bufferOffset = _serializer.float64(obj.q3, buffer, bufferOffset);
    // Serialize message field [q4]
    bufferOffset = _serializer.float64(obj.q4, buffer, bufferOffset);
    // Serialize message field [q5]
    bufferOffset = _serializer.float64(obj.q5, buffer, bufferOffset);
    // Serialize message field [q6]
    bufferOffset = _serializer.float64(obj.q6, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointVariables
    let len;
    let data = new JointVariables(null);
    // Deserialize message field [q1]
    data.q1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q2]
    data.q2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q3]
    data.q3 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q4]
    data.q4 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q5]
    data.q5 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [q6]
    data.q6 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fk/JointVariables';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a61a219e6f5b1a7fbfc4c6ce5b5c4482';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 q1
    float64 q2
    float64 q3
    float64 q4
    float64 q5
    float64 q6
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JointVariables(null);
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

    if (msg.q3 !== undefined) {
      resolved.q3 = msg.q3;
    }
    else {
      resolved.q3 = 0.0
    }

    if (msg.q4 !== undefined) {
      resolved.q4 = msg.q4;
    }
    else {
      resolved.q4 = 0.0
    }

    if (msg.q5 !== undefined) {
      resolved.q5 = msg.q5;
    }
    else {
      resolved.q5 = 0.0
    }

    if (msg.q6 !== undefined) {
      resolved.q6 = msg.q6;
    }
    else {
      resolved.q6 = 0.0
    }

    return resolved;
    }
};

module.exports = JointVariables;
