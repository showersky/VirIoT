/*
 * Copyright 2015 Telefonica Investigación y Desarrollo, S.A.U
 *
 * This file is part of iotagent-json
 *
 * iotagent-json is free software: you can redistribute it and/or
 * modify it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the License,
 * or (at your option) any later version.
 *
 * iotagent-json is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public
 * License along with iotagent-json.
 * If not, seehttp://www.gnu.org/licenses/.
 *
 * For those usages not covered by the GNU Affero General Public License
 * please contact with::[contacto@tid.es]
 */
var config = {};

config.mqtt = {
    host: 'mosquitto',
    port: 1883,
    thinkingThingsPlugin: true,
    qos: 0,
    retain: false
};

config.amqp = {
    host: 'localhost',
    port: 5672,
    exchange: 'iota-exchange',
    queue: 'iotaqueue',
    options: { durable: true }
};

config.http = {
    port: 7896
};

config.iota = {
    logLevel: 'DEBUG',
    timestamp: true,
    contextBroker: {
        host: 'orion',
        port: '1026'
    },
    server: {
        port: 4041
    },
    deviceRegistry: {
        type: 'mongodb'
    },
    mongodb: {
        host: 'mongo',
        port: '27017',
        db: 'iotagentjson'
    },
    types: {},
    service: 'howtoService',
    subservice: '/howto',
    providerUrl: 'http://iotagent:4041',
    deviceRegistrationDuration: 'P20Y',
    defaultType: 'Thing',
    defaultResource: '/iot/json'
};

config.configRetrieval = false;
config.defaultKey = 'fed4iot';
config.defaultTransport = 'MQTT';

module.exports = config;
