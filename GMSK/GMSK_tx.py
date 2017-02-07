#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gmsk Tx
# Generated: Fri Jan 27 17:50:00 2017
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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class GMSK_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Gmsk Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Gmsk Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "GMSK_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.rate = rate = 500e3
        self.eb = eb = 0.35
        self.samp_rate = samp_rate = rate
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(20, 10, 1.0/float(sps), eb, 45*sps)
        self.gain_RF = gain_RF = 0
        self.cf = cf = 5e9
        self.GN = GN = 0

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, 'Freq')
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, 'Const')
        self.controls_widget_2 = Qt.QWidget()
        self.controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_2)
        self.controls_grid_layout_2 = Qt.QGridLayout()
        self.controls_layout_2.addLayout(self.controls_grid_layout_2)
        self.controls.addTab(self.controls_widget_2, 'time')
        self.top_layout.addWidget(self.controls)
        self._GN_range = Range(0, 1, 0.05, 0, 200)
        self._GN_win = RangeWidget(self._GN_range, self.set_GN, "GN", "counter_slider", float)
        self.top_layout.addWidget(self._GN_win)
        self._rate_range = Range(50e3, 1000e3, 100, 500e3, 200)
        self._rate_win = RangeWidget(self._rate_range, self.set_rate, 'Sample Rate', "counter_slider", float)
        self.top_layout.addWidget(self._rate_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024*8, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(0, 200)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.controls_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win,  0,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Freq spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['QPSK mod', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.controls_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win,  0,0,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['QPSK_mod', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.controls_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win,  0,0,1,1)
        self._gain_RF_range = Range(0, 31.5, 0.5, 0, 200)
        self._gain_RF_win = RangeWidget(self._gain_RF_range, self.set_gain_RF, "gain_RF", "counter_slider", float)
        self.top_layout.addWidget(self._gain_RF_win)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28/100.0, (rrc_taps), 32, 16, 1.5, 1)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=sps,
        	bt=0.3,
        	verbose=False,
        	log=False,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/unal/Desktop/USRP--UNAL/LabWC/GMSK/plaindata.dat', True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/unal/Desktop/USRP--UNAL/LabWC/GMSK/vecdata', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/unal/Desktop/USRP--UNAL/LabWC/GMSK/crc32test', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=3,
        		preamble='0000000000000000',
        		access_code='1111111111111111111111111111111111111111111111111111111111111111',
        		pad_for_usrp=False,
        	),
        	payload_length=1,
        )
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, GN, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "GMSK_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(20, 10, 1.0/float(self.sps), self.eb, 45*self.sps))

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate
        self.set_samp_rate(self.rate)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_taps(firdes.root_raised_cosine(20, 10, 1.0/float(self.sps), self.eb, 45*self.sps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_gain_RF(self):
        return self.gain_RF

    def set_gain_RF(self, gain_RF):
        self.gain_RF = gain_RF

    def get_cf(self):
        return self.cf

    def set_cf(self, cf):
        self.cf = cf

    def get_GN(self):
        return self.GN

    def set_GN(self, GN):
        self.GN = GN
        self.analog_noise_source_x_0.set_amplitude(self.GN)


def main(top_block_cls=GMSK_tx, options=None):

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
