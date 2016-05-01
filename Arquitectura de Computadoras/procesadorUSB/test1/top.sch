<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="spartan3e" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="rxf" />
        <signal name="txe" />
        <signal name="clk" />
        <signal name="rst" />
        <signal name="dataUSB(7:0)" />
        <signal name="rd" />
        <signal name="XLXN_1" />
        <signal name="XLXN_2" />
        <signal name="leds(7:0)" />
        <port polarity="Input" name="rxf" />
        <port polarity="Input" name="txe" />
        <port polarity="Input" name="clk" />
        <port polarity="Input" name="rst" />
        <port polarity="Input" name="dataUSB(7:0)" />
        <port polarity="Output" name="rd" />
        <port polarity="Output" name="leds(7:0)" />
        <blockdef name="uart">
            <timestamp>2015-5-13T0:45:22</timestamp>
            <rect width="256" x="64" y="-384" height="384" />
            <line x2="0" y1="-352" y2="-352" x1="64" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-352" y2="-352" x1="320" />
            <line x2="384" y1="-192" y2="-192" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
        <blockdef name="desplegador">
            <timestamp>2015-5-13T1:46:7</timestamp>
            <rect width="256" x="64" y="-192" height="192" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
        </blockdef>
        <block symbolname="uart" name="XLXI_1">
            <blockpin signalname="rxf" name="rxf" />
            <blockpin signalname="txe" name="txe" />
            <blockpin signalname="XLXN_2" name="rd_u" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="dataUSB(7:0)" name="dataUSB(7:0)" />
            <blockpin signalname="rd" name="rd" />
            <blockpin signalname="XLXN_1" name="da" />
            <blockpin signalname="leds(7:0)" name="dato(7:0)" />
        </block>
        <block symbolname="desplegador" name="XLXI_2">
            <blockpin signalname="XLXN_1" name="da" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="XLXN_2" name="rd_u" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <instance x="832" y="1120" name="XLXI_1" orien="R0">
        </instance>
        <branch name="rxf">
            <wire x2="832" y1="768" y2="768" x1="800" />
        </branch>
        <iomarker fontsize="28" x="800" y="768" name="rxf" orien="R180" />
        <branch name="txe">
            <wire x2="832" y1="832" y2="832" x1="800" />
        </branch>
        <iomarker fontsize="28" x="800" y="832" name="txe" orien="R180" />
        <branch name="clk">
            <wire x2="752" y1="960" y2="960" x1="672" />
            <wire x2="800" y1="960" y2="960" x1="752" />
            <wire x2="816" y1="960" y2="960" x1="800" />
            <wire x2="832" y1="960" y2="960" x1="816" />
            <wire x2="800" y1="960" y2="976" x1="800" />
            <wire x2="816" y1="976" y2="976" x1="800" />
            <wire x2="816" y1="976" y2="1184" x1="816" />
            <wire x2="1280" y1="1184" y2="1184" x1="816" />
            <wire x2="1280" y1="992" y2="1184" x1="1280" />
            <wire x2="1456" y1="992" y2="992" x1="1280" />
        </branch>
        <branch name="rst">
            <wire x2="832" y1="1024" y2="1024" x1="800" />
        </branch>
        <iomarker fontsize="28" x="800" y="1024" name="rst" orien="R180" />
        <branch name="dataUSB(7:0)">
            <wire x2="832" y1="1088" y2="1088" x1="800" />
        </branch>
        <iomarker fontsize="28" x="800" y="1088" name="dataUSB(7:0)" orien="R180" />
        <branch name="rd">
            <wire x2="1248" y1="768" y2="768" x1="1216" />
        </branch>
        <iomarker fontsize="28" x="1248" y="768" name="rd" orien="R0" />
        <instance x="1456" y="1088" name="XLXI_2" orien="R0">
        </instance>
        <branch name="XLXN_1">
            <wire x2="1456" y1="928" y2="928" x1="1216" />
        </branch>
        <iomarker fontsize="28" x="672" y="960" name="clk" orien="R180" />
        <branch name="XLXN_2">
            <wire x2="624" y1="656" y2="896" x1="624" />
            <wire x2="832" y1="896" y2="896" x1="624" />
            <wire x2="1904" y1="656" y2="656" x1="624" />
            <wire x2="1904" y1="656" y2="928" x1="1904" />
            <wire x2="1904" y1="928" y2="928" x1="1840" />
        </branch>
        <branch name="leds(7:0)">
            <wire x2="1248" y1="1088" y2="1088" x1="1216" />
        </branch>
        <iomarker fontsize="28" x="1248" y="1088" name="leds(7:0)" orien="R0" />
    </sheet>
</drawing>