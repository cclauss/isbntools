#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Exceptions for isbntools.dev

The classes in isbntools.dev should use the exceptions below.
"""


class ISBNToolsDevException(Exception):
    """ Base class for isbntools.dev exceptions

    This exception should not be raised directly,
    only subclasses of this exception should be used!
    """

    def __init__(self, msg=None):
        if msg:
            self.message = '%s (%s)' % (self.message, msg)

    def __str__(self):
        return getattr(self, 'message', '')       # pragma: no cover


class ITHTTPError(ISBNToolsDevException):
    """ Exception raised for HTTP related errors
    """
    message = "an HTTP error has ocurred"


class ITURLError(ISBNToolsDevException):
    """ Exception raised for URL related errors
    """
    message = "an URL error has ocurred"


class DataNotFoundError(ISBNToolsDevException):
    """ Exception raised when there is no target data from the service
    """
    message = "the target data was not found"


class ServiceIsDownError(ISBNToolsDevException):
    """ Exception raised when the service is not available
    """
    message = "the service is down (try later)"


class DataWrongShapeError(ISBNToolsDevException):
    """ Exception raised when the data hasn't the expected format
    """
    message = "the data hasn't the expected format"


class DataNotFoundError(ISBNToolsDevException):
    """ Exception raised when the data isn't availabe at the service
    """
    message = "the data isn't available at this service"


class NotValidMetadataError(ISBNToolsDevException):
    """ Exception raised when the metadata hasn't the expected format
    """
    message = "the metadata hasn't the expected format"


class RecordMappingError(ISBNToolsDevException):
    """ Exception raised when the mapping records -> canonical doesn't work
    """
    message = "the mapping `canonical <- records` doesn't work"


class NoAPIKeyError(ISBNToolsDevException):
    """ Exception raised when the API Key for a service is not found
    """
    message = "this service needs an API key"


class NotImplementedError(ISBNToolsDevException):
    """ Exception raised when the methods wasn't implemented yet!
    """
    message = "this method wasn't implemented yet"
