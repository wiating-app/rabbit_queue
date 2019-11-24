#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rabbit_queue` package."""


import pytest

from rabbit_queue.rabbit_queue import RabbitQueue


QUEUE_NAME = 'some name'


@pytest.fixture
def pika_mock(mocker):
    mocker.patch('rabbit_queue.rabbit_queue.pika', autospec=True)


@pytest.fixture
def rabbit_queue_mock(pika_mock):
    return RabbitQueue(queue_name=QUEUE_NAME)


def test_createObject(rabbit_queue_mock):
    pass


def test_publish(rabbit_queue_mock):
    rabbit_queue_mock.publish('some body')


def some_callback():
    pass


def test_consume(rabbit_queue_mock):
    rabbit_queue_mock.consume(some_callback)

