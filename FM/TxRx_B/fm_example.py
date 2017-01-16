#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Example
# Generated: Mon Jan 16 11:49:27 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
import time
from gnuradio import qtgui


class fm_example(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Example")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fm_example")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 1
        self.rx_sr = rx_sr = 1e6
        self.qa_rate = qa_rate = 200e3
        self.cf = cf = 2.45e9
        self.a_rate = a_rate = 44.1e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 1, 0.1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, "volume", "counter_slider", float)
        self.top_layout.addWidget(self._volume_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(rx_sr)
        self.uhd_usrp_sink_0.set_center_freq(2.45e9, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=int(rx_sr),
                decimation=int(a_rate),
                taps=None,
                fractional_bw=None,
        )
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, 'Freq_RX')
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, 'Time_RX')
        self.controls_widget_2 = Qt.QWidget()
        self.controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_2)
        self.controls_grid_layout_2 = Qt.QGridLayout()
        self.controls_layout_2.addLayout(self.controls_grid_layout_2)
        self.controls.addTab(self.controls_widget_2, 'Freq_TX')
        self.controls_widget_3 = Qt.QWidget()
        self.controls_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_3)
        self.controls_grid_layout_3 = Qt.QGridLayout()
        self.controls_layout_3.addLayout(self.controls_grid_layout_3)
        self.controls.addTab(self.controls_widget_3, 'Time_TX')
        self.top_layout.addWidget(self.controls)
        self._cf_range = Range(2e9, 3e9, 0.1e9, 2.45e9, 200)
        self._cf_win = RangeWidget(self._cf_range, self.set_cf, "cf", "counter_slider", float)
        self.top_layout.addWidget(self._cf_win)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((0.5, ))
        self.audio_source_0 = audio.source(44100, '', False)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=int(a_rate),
        	quad_rate=int(a_rate),
        	tau=75e-6,
        	max_dev=20e3,
        	fh=-1.0,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_example")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_rx_sr(self):
        return self.rx_sr

    def set_rx_sr(self, rx_sr):
        self.rx_sr = rx_sr
        self.uhd_usrp_sink_0.set_samp_rate(self.rx_sr)

    def get_qa_rate(self):
        return self.qa_rate

    def set_qa_rate(self, qa_rate):
        self.qa_rate = qa_rate

    def get_cf(self):
        return self.cf

    def set_cf(self, cf):
        self.cf = cf

    def get_a_rate(self):
        return self.a_rate

    def set_a_rate(self, a_rate):
        self.a_rate = a_rate


def main(top_block_cls=fm_example, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
