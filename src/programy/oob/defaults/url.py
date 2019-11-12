"""
Copyright (c) 2016-2019 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from programy.utils.parsing.linenumxml import LineNumberingParser
import xml.etree.ElementTree as ET  # pylint: disable=wrong-import-order
from programy.utils.logging.ylogger import YLogger
from programy.oob.defaults.oob import OutOfBandProcessor


class URLOutOfBandProcessor(OutOfBandProcessor):
    """
    <oob>
        <url>http://<star/>.com</url>
    </oob>
    """
    def __init__(self):
        OutOfBandProcessor.__init__(self)
        self._url = None

    def parse_oob_xml(self, oob: ET.Element):
        if oob is not None and oob.text is not None:
            self._url = oob.text
            return True
        else:
            YLogger.error(self, "Unvalid url oob command - missing url!")
            return False

    def execute_oob_command(self, client_context):
        YLogger.info(client_context, "URLOutOfBandProcessor: Loading=%s", self._url)
        return "URL"
