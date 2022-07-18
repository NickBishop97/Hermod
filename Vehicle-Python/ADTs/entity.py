# Copyright 2022 Proyectos y Sistemas de Mantenimiento SL (eProsima).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
entity.py
"""
from threading import Thread
# from email.message import Message
# from logging.config import listen
# from multiprocessing.connection import Listener
from threading import Condition
# import time
from queue import Queue

import fastdds

DESCRIPTION = """Writer and Reader ADTs for use"""
USAGE = """TO BE INHERITED BY A USER DEFINED CLASS"""
<<<<<<< HEAD
=======

>>>>>>> master

class Entity:

    class ReaderListener(fastdds.DataReaderListener):

        def __init__(self):
            # self.__data = __data
            super().__init__()

        def on_subscription_matched(self, datareader, info):
            if(0 < info.current_count_change):
                print("Subscriber matched publisher {}".format(info.last_publication_handle))
            else:
                print("Subscriber unmatched publisher {}".format(info.last_publication_handle))
                exit()
<<<<<<< HEAD
            
=======

>>>>>>> master
        def on_data_available(self, reader):
            raise NotImplementedError(self.____class__.__name__ + " was not implemented!")

        def getDataReturn(self):
            raise NotImplementedError(self.____class__.__name__ + " was not implemented!")

    class Reader:
        def __init__(self,
                     ddsDataArray,):

            # SAVING INPUT VARIABLES
<<<<<<< HEAD
            self.__MessageType = ddsDataArray[0]
            self.__MessageType_name = ddsDataArray[1]
            self.__Topic_name = ddsDataArray[2]
            
=======
            self.MessageType = ddsDataArray[0]
            self.MessageType_name = ddsDataArray[1]
            self.Topic_name = ddsDataArray[2]

>>>>>>> master
            try:
                # __data = HelloWorld.HelloWorld()
                func = getattr(self.__MessageType, f"{self.__MessageType_name}")  # inputting the idl special datatype
                self.__data = func()
            except AttributeError:
<<<<<<< HEAD
                print(f"{self.__MessageType_name}.{self.__MessageType_name}() not found")
=======
                print(f"{self.MessageType_name}.{self.MessageType_name}() not found")
>>>>>>> master
                raise

            # use factory to make participant
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.__participant_qos)
            self.__participant = factory.create_participant(0, self.__participant_qos)

            # create name and initialize the __data type for the topic
            # myPubSubType() is the message type being defined
            try:
                funcOne = getattr(self.__MessageType, f"{self.__MessageType_name}PubSubType")  # inputting the idl special datatype
                self.__topic_data_type = funcOne()
                print(f"Found: {self.__MessageType_name}.{self.__MessageType_name}PubSubType()")
            except AttributeError:
<<<<<<< HEAD
                print(f"{self.__MessageType_name}.{self.__MessageType_name}PubSubType() not found")
                raise

            #creation of a topic name and registering __data type and topic with fastdds
            self.__topic_data_type.setName(f"{self.__MessageType_name}")
            self.__type_support = fastdds.TypeSupport(self.__topic_data_type)
            self.__participant.register_type(self.__type_support)
=======
                print(f"{self.MessageType_name}.{self.MessageType_name}PubSubType() not found")
                raise

            # creation of a topic name and registering data type and topic with fastdds
            self.topic_data_type.setName(f"{self.MessageType_name}")
            self.type_support = fastdds.TypeSupport(self.topic_data_type)
            self.participant.register_type(self.type_support)
>>>>>>> master

            # create the topic itself and name it
            self.__topic_qos = fastdds.TopicQos()
            self.__participant.get_default_topic_qos(self.__topic_qos)
            self.__topic = self.__participant.create_topic(f"{self.__Topic_name}", self.__topic_data_type.getName(), self.__topic_qos)

            # create the particular subscriber
            self.__subscriber_qos = fastdds.SubscriberQos()
            self.__participant.get_default_subscriber_qos(self.__subscriber_qos)
            self.__subscriber = self.__participant.create_subscriber(self.__subscriber_qos)

            # create the __data reader object, and listen to the topic

            #####################################################################################################

            self.__listener = ddsDataArray[3](self.__data)
            #This should get a Queue() by reference from the listener object
            self.__dataQueue = self.__listener.getDataReturn() 

            #####################################################################################################
<<<<<<< HEAD
           
            #creation of the __data reader
            self.__reader_qos = fastdds.DataReaderQos()
            self.__subscriber.get_default_datareader_qos(self.__reader_qos)
            self.__reader = self.__subscriber.create_datareader(self.__topic, self.__reader_qos, self.__listener)

        def getDataQueue(self) -> Queue:
            return self.__dataQueue
=======

            # creation of the data reader
            self.reader_qos = fastdds.DataReaderQos()
            self.subscriber.get_default_datareader_qos(self.reader_qos)
            self.reader = self.subscriber.create_datareader(self.topic, self.reader_qos, self.listener)
>>>>>>> master

        def dataRunReturn(self) -> Queue:
            while True:
                if not self.__dataQueue.empty():
                    return self.__dataQueue
                else:
                    return None

        def run(self) -> None:
            dataThread = Thread(target=(self.dataRunReturn), daemon=True)
            dataThread.start()

        def delete(self) -> None:
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant.delete_contained_entities()
            factory.delete_participant(self.__participant)

    class WriterListener (fastdds.DataWriterListener):
        def __init__(self, writer):
            self.__writer = writer
            super().__init__()

<<<<<<< HEAD
        def on_publication_matched(self, datawriter, info) -> None:
            print("Sending...")
            if(0 < info.current_count_change):
                print("Publisher matched subscriber {}".format(info.last_subscription_handle))
                
                self.__writer._cvDiscovery.acquire()
                self.__writer._cvDiscovery.notify()
                self.__writer._matched_reader += 1
                self.__writer._cvDiscovery.release()
            else:
                print("Publisher unmatched subscriber {}".format(info.last_subscription_handle))
                self.__writer._cvDiscovery.acquire()
                self.__writer._matched_reader -= 1
                self.__writer._cvDiscovery.notify()
                self.__writer._cvDiscovery.release()
                #exit() #kills flask
=======
        def on_publication_matched(self, datawriter, info):
            print("Sending...")
            if(0 < info.current_count_change):
                print("Publisher matched subscriber {}".format(info.last_subscription_handle))

                self._writer._cvDiscovery.acquire()
                self._writer._cvDiscovery.notify()
                self._writer._matched_reader += 1
                self._writer._cvDiscovery.release()
            else:
                print("Publisher unmatched subscriber {}".format(info.last_subscription_handle))
                self._writer._cvDiscovery.acquire()
                self._writer._matched_reader -= 1
                self._writer._cvDiscovery.notify()
                self._writer._cvDiscovery.release()
                # exit()  # kills flask
>>>>>>> master

    class Writer:

        def __init__(self, ddsDataArray):
            # SAVING INPUT VARIABLES
<<<<<<< HEAD
            self.__MessageType      = ddsDataArray[0]
            self.__MessageType_name = ddsDataArray[1]
            self.__Topic_name       = ddsDataArray[2]
=======
            self.MessageType = ddsDataArray[0]
            self.MessageType_name = ddsDataArray[1]
            self.Topic_name = ddsDataArray[2]
>>>>>>> master

            # SAVING THE DATA TYPE OF THE MESSAGE
            try:
                # __data = HelloWorld.HelloWorld()
                func = getattr(self.__MessageType, f"{self.__MessageType_name}")  # inputting the idl special datatype
                self.__data = func()
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}() not found")

            self.___matched_reader = 0
            self.___cvDiscovery = Condition()
            self.__index = 0

            # creating a fastdds factory to generate participant.
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant_qos = fastdds.DomainParticipantQos()
            factory.get_default_participant_qos(self.__participant_qos)
            self.__participant = factory.create_participant(0, self.__participant_qos)

            # myPubSubType() is the message type being defined
            try:
                funcOne = getattr(self.__MessageType, f"{self.__MessageType_name}PubSubType")  # inputting the idl special datatype
                self.__topic_data_type = funcOne()
                print(f"Found: {self.__MessageType_name}.{self.__MessageType_name}PubSubType()")
            except AttributeError:
                print(f"{self.__MessageType_name}.{self.__MessageType_name}PubSubType() not found")

            self.__topic_data_type.setName(f"{self.__MessageType_name}")  # setting name of topic to myPubSubType_name, <idl-name>
            self.__type_support = fastdds.TypeSupport(self.__topic_data_type)
            self.__participant.register_type(self.__type_support)

            # creating a topic using the topic name and idl file name
            self.__topic_qos = fastdds.TopicQos()
            self.__participant.get_default_topic_qos(self.__topic_qos)
            self.__topic = self.__participant.create_topic(self.__Topic_name, self.__topic_data_type.getName(), self.__topic_qos)

            # making the participant a publisher
            self.__publisher_qos = fastdds.PublisherQos()
            self.__participant.get_default_publisher_qos(self.__publisher_qos)
            self.__publisher = self.__participant.create_publisher(self.__publisher_qos)

            # making a __data writer
            self.__listener = Entity.WriterListener(self)
            self.__writer_qos = fastdds.DataWriterQos()
            self.__publisher.get_default_datawriter_qos(self.__writer_qos)
            self.__writer = self.__publisher.create_datawriter(self.__topic, self.__writer_qos, self.__listener)

        def wait_discovery(self) -> None:
            self.___cvDiscovery.acquire()
            print(f"{self.__MessageType_name}Writer is waiting discovery...")
            self.___cvDiscovery.wait_for(lambda: self.___matched_reader != 0)
            self.___cvDiscovery.release()
            print("Writer discovery finished...")

        def delete(self) -> None:
            factory = fastdds.DomainParticipantFactory.get_instance()
            self.__participant.delete_contained_entities()
            factory.delete_participant(self.__participant)
    