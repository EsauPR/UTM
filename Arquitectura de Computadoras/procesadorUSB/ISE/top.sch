<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="spartan3e" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="XLXN_1" />
        <signal name="XLXN_3(7:0)" />
        <signal name="rxf" />
        <signal name="txe" />
        <signal name="rst" />
        <signal name="dataUSB(7:0)" />
        <signal name="XLXN_21(10:0)" />
        <signal name="XLXN_30" />
        <signal name="XLXN_34(9:0)" />
        <signal name="XLXN_36" />
        <signal name="rd" />
        <signal name="XLXN_41(7:0)" />
        <signal name="XLXN_52" />
        <signal name="XLXN_59" />
        <signal name="clk" />
        <signal name="XLXN_63" />
        <signal name="XLXN_85" />
        <signal name="XLXN_86(4:0)" />
        <signal name="XLXN_87(4:0)" />
        <signal name="XLXN_90" />
        <signal name="XLXN_92(7:0)" />
        <signal name="XLXN_100(7:0)" />
        <signal name="leds(7:0)" />
        <signal name="XLXN_104(15:0)" />
        <signal name="XLXN_105(15:0)" />
        <port polarity="Input" name="rxf" />
        <port polarity="Input" name="txe" />
        <port polarity="Input" name="rst" />
        <port polarity="Input" name="dataUSB(7:0)" />
        <port polarity="Output" name="rd" />
        <port polarity="Input" name="clk" />
        <port polarity="Output" name="leds(7:0)" />
        <blockdef name="uart">
            <timestamp>2015-5-27T1:6:41</timestamp>
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
        <blockdef name="ucp">
            <timestamp>2015-5-27T1:6:36</timestamp>
            <line x2="384" y1="32" y2="32" x1="320" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-208" y2="-208" x1="64" />
            <line x2="0" y1="-128" y2="-128" x1="64" />
            <rect width="64" x="0" y="-60" height="24" />
            <line x2="0" y1="-48" y2="-48" x1="64" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <rect width="64" x="320" y="-108" height="24" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
            <rect width="256" x="64" y="-320" height="448" />
        </blockdef>
        <blockdef name="UC">
            <timestamp>2015-5-27T2:25:40</timestamp>
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <rect width="64" x="320" y="-236" height="24" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
            <rect width="256" x="64" y="-256" height="320" />
        </blockdef>
        <blockdef name="ramb16_s9_s18">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <rect width="64" x="544" y="-960" height="32" />
            <rect width="64" x="0" y="-1104" height="32" />
            <line x2="64" y1="-1152" y2="-640" x1="64" />
            <line x2="64" y1="-640" y2="-640" x1="128" />
            <line x2="128" y1="-576" y2="-640" x1="128" />
            <line x2="128" y1="-576" y2="-576" x1="64" />
            <line x2="64" y1="-64" y2="-576" x1="64" />
            <line x2="64" y1="-64" y2="-64" x1="544" />
            <line x2="544" y1="-576" y2="-64" x1="544" />
            <line x2="544" y1="-576" y2="-576" x1="480" />
            <line x2="480" y1="-640" y2="-576" x1="480" />
            <line x2="480" y1="-640" y2="-640" x1="544" />
            <line x2="64" y1="-1152" y2="-1152" x1="544" />
            <line x2="544" y1="-640" y2="-1152" x1="544" />
            <rect width="64" x="544" y="-368" height="32" />
            <rect width="64" x="0" y="-144" height="32" />
            <rect width="64" x="0" y="-208" height="32" />
            <rect width="64" x="544" y="-880" height="32" />
            <line x2="64" y1="-832" y2="-848" x1="80" />
            <line x2="80" y1="-816" y2="-832" x1="64" />
            <rect width="64" x="0" y="-720" height="32" />
            <rect width="64" x="0" y="-784" height="32" />
            <rect width="64" x="0" y="-272" height="32" />
            <line x2="64" y1="-320" y2="-336" x1="80" />
            <line x2="80" y1="-304" y2="-320" x1="64" />
            <rect width="64" x="544" y="-432" height="32" />
            <line x2="544" y1="-944" y2="-944" x1="608" />
            <line x2="64" y1="-1088" y2="-1088" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="544" y1="-352" y2="-352" x1="608" />
            <line x2="544" y1="-416" y2="-416" x1="608" />
            <line x2="64" y1="-192" y2="-192" x1="0" />
            <line x2="544" y1="-864" y2="-864" x1="608" />
            <line x2="64" y1="-704" y2="-704" x1="0" />
            <line x2="64" y1="-1024" y2="-1024" x1="0" />
            <line x2="64" y1="-768" y2="-768" x1="0" />
            <line x2="64" y1="-256" y2="-256" x1="0" />
            <line x2="64" y1="-320" y2="-320" x1="0" />
            <line x2="64" y1="-384" y2="-384" x1="0" />
            <line x2="64" y1="-448" y2="-448" x1="0" />
            <line x2="64" y1="-512" y2="-512" x1="0" />
            <line x2="64" y1="-832" y2="-832" x1="0" />
            <line x2="64" y1="-896" y2="-896" x1="0" />
            <line x2="64" y1="-960" y2="-960" x1="0" />
        </blockdef>
        <blockdef name="gnd">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-96" x1="64" />
            <line x2="52" y1="-48" y2="-48" x1="76" />
            <line x2="60" y1="-32" y2="-32" x1="68" />
            <line x2="40" y1="-64" y2="-64" x1="88" />
            <line x2="64" y1="-64" y2="-80" x1="64" />
            <line x2="64" y1="-128" y2="-96" x1="64" />
        </blockdef>
        <blockdef name="vcc">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-64" x1="64" />
            <line x2="64" y1="0" y2="-32" x1="64" />
            <line x2="32" y1="-64" y2="-64" x1="96" />
        </blockdef>
        <blockdef name="AR">
            <timestamp>2015-5-27T0:44:57</timestamp>
            <rect width="256" x="64" y="-320" height="320" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <rect width="64" x="0" y="-172" height="24" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <rect width="64" x="0" y="-108" height="24" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <rect width="64" x="320" y="-300" height="24" />
            <line x2="384" y1="-288" y2="-288" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
        <blockdef name="MUX">
            <timestamp>2015-5-27T0:45:1</timestamp>
            <rect width="256" x="64" y="-192" height="192" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <rect width="64" x="0" y="-108" height="24" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <rect width="64" x="320" y="-172" height="24" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
        </blockdef>
        <blockdef name="PU">
            <timestamp>2015-5-27T1:6:21</timestamp>
            <rect width="256" x="64" y="-320" height="320" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-288" y2="-288" x1="320" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <rect width="64" x="320" y="-172" height="24" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <rect width="64" x="320" y="-108" height="24" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
        </blockdef>
        <block symbolname="uart" name="XLXI_1">
            <blockpin signalname="rxf" name="rxf" />
            <blockpin signalname="txe" name="txe" />
            <blockpin signalname="XLXN_59" name="rd_u" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="dataUSB(7:0)" name="dataUSB(7:0)" />
            <blockpin signalname="rd" name="rd" />
            <blockpin signalname="XLXN_1" name="da" />
            <blockpin signalname="XLXN_3(7:0)" name="dato(7:0)" />
        </block>
        <block symbolname="ucp" name="XLXI_2">
            <blockpin signalname="XLXN_1" name="DA" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="XLXN_3(7:0)" name="datoRX(7:0)" />
            <blockpin signalname="XLXN_36" name="WR" />
            <blockpin signalname="XLXN_30" name="P_OK" />
            <blockpin signalname="XLXN_59" name="RD" />
            <blockpin signalname="XLXN_41(7:0)" name="dato(7:0)" />
            <blockpin signalname="XLXN_21(10:0)" name="dir(10:0)" />
        </block>
        <block symbolname="UC" name="XLXI_3">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="XLXN_30" name="P_OK" />
            <blockpin signalname="XLXN_104(15:0)" name="IR(15:0)" />
            <blockpin signalname="XLXN_105(15:0)" name="dato(15:0)" />
            <blockpin signalname="XLXN_34(9:0)" name="PC(9:0)" />
        </block>
        <block symbolname="ramb16_s9_s18" name="XLXI_4">
            <attr value="0000000000000000000000000000000000000000000000000000000000111111" name="INIT_00">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="0200020002000200020002000200020002000200020002000200020002000200" name="INIT_01">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="0300030003000300030003000300030003000300030003000300030003000300" name="INIT_02">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <blockpin signalname="XLXN_21(10:0)" name="ADDRA(10:0)" />
            <blockpin signalname="XLXN_34(9:0)" name="ADDRB(9:0)" />
            <blockpin signalname="clk" name="CLKA" />
            <blockpin signalname="clk" name="CLKB" />
            <blockpin signalname="XLXN_41(7:0)" name="DIA(7:0)" />
            <blockpin name="DIB(15:0)" />
            <blockpin name="DIPA(0:0)" />
            <blockpin name="DIPB(1:0)" />
            <blockpin signalname="XLXN_63" name="ENA" />
            <blockpin signalname="XLXN_63" name="ENB" />
            <blockpin signalname="XLXN_52" name="SSRA" />
            <blockpin signalname="XLXN_52" name="SSRB" />
            <blockpin signalname="XLXN_36" name="WEA" />
            <blockpin signalname="XLXN_52" name="WEB" />
            <blockpin name="DOA(7:0)" />
            <blockpin signalname="XLXN_104(15:0)" name="DOB(15:0)" />
            <blockpin name="DOPA(0:0)" />
            <blockpin name="DOPB(1:0)" />
        </block>
        <block symbolname="gnd" name="XLXI_5">
            <blockpin signalname="XLXN_52" name="G" />
        </block>
        <block symbolname="vcc" name="XLXI_6">
            <blockpin signalname="XLXN_63" name="P" />
        </block>
        <block symbolname="AR" name="XLXI_7">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="XLXN_85" name="ctr" />
            <blockpin signalname="XLXN_86(4:0)" name="AddrRd(4:0)" />
            <blockpin signalname="XLXN_87(4:0)" name="AddrRr(4:0)" />
            <blockpin signalname="leds(7:0)" name="DataIn(7:0)" />
            <blockpin signalname="XLXN_92(7:0)" name="Rr(7:0)" />
            <blockpin name="Rd(7:0)" />
        </block>
        <block symbolname="MUX" name="XLXI_9">
            <blockpin signalname="XLXN_90" name="sel" />
            <blockpin signalname="XLXN_100(7:0)" name="D1(7:0)" />
            <blockpin signalname="XLXN_92(7:0)" name="D0(7:0)" />
            <blockpin signalname="leds(7:0)" name="SALIDA(7:0)" />
        </block>
        <block symbolname="PU" name="XLXI_10">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="XLXN_105(15:0)" name="CO(15:0)" />
            <blockpin signalname="XLXN_85" name="wr" />
            <blockpin signalname="XLXN_90" name="sel" />
            <blockpin signalname="XLXN_86(4:0)" name="AddrRd(4:0)" />
            <blockpin signalname="XLXN_87(4:0)" name="AddrRr(4:0)" />
            <blockpin signalname="XLXN_100(7:0)" name="constante(7:0)" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <instance x="768" y="1248" name="XLXI_1" orien="R0">
        </instance>
        <branch name="XLXN_3(7:0)">
            <wire x2="1168" y1="1216" y2="1216" x1="1152" />
            <wire x2="1168" y1="1216" y2="1296" x1="1168" />
            <wire x2="1312" y1="1296" y2="1296" x1="1168" />
        </branch>
        <branch name="XLXN_1">
            <wire x2="1312" y1="1056" y2="1056" x1="1152" />
        </branch>
        <instance x="1312" y="1344" name="XLXI_2" orien="R0">
        </instance>
        <branch name="rst">
            <wire x2="736" y1="1152" y2="1152" x1="224" />
            <wire x2="768" y1="1152" y2="1152" x1="736" />
            <wire x2="736" y1="1152" y2="1328" x1="736" />
            <wire x2="1232" y1="1328" y2="1328" x1="736" />
            <wire x2="736" y1="1328" y2="1824" x1="736" />
            <wire x2="1504" y1="1824" y2="1824" x1="736" />
            <wire x2="1232" y1="1216" y2="1328" x1="1232" />
            <wire x2="1312" y1="1216" y2="1216" x1="1232" />
        </branch>
        <branch name="dataUSB(7:0)">
            <wire x2="768" y1="1216" y2="1216" x1="720" />
        </branch>
        <iomarker fontsize="28" x="720" y="1216" name="dataUSB(7:0)" orien="R180" />
        <branch name="XLXN_21(10:0)">
            <wire x2="1952" y1="1312" y2="1312" x1="1696" />
            <wire x2="1952" y1="1184" y2="1312" x1="1952" />
            <wire x2="2224" y1="1184" y2="1184" x1="1952" />
        </branch>
        <branch name="XLXN_36">
            <wire x2="1920" y1="1376" y2="1376" x1="1696" />
            <wire x2="1920" y1="928" y2="1376" x1="1920" />
            <wire x2="2224" y1="928" y2="928" x1="1920" />
        </branch>
        <branch name="rd">
            <wire x2="1296" y1="896" y2="896" x1="1152" />
        </branch>
        <branch name="XLXN_41(7:0)">
            <wire x2="1776" y1="1248" y2="1248" x1="1696" />
            <wire x2="1776" y1="1152" y2="1248" x1="1776" />
            <wire x2="2144" y1="1152" y2="1152" x1="1776" />
            <wire x2="2144" y1="1152" y2="1248" x1="2144" />
            <wire x2="2224" y1="1248" y2="1248" x1="2144" />
        </branch>
        <instance x="3056" y="1056" name="XLXI_6" orien="R0" />
        <instance x="2080" y="2144" name="XLXI_5" orien="R0" />
        <branch name="XLXN_34(9:0)">
            <wire x2="2048" y1="1760" y2="1760" x1="1888" />
            <wire x2="2048" y1="1696" y2="1760" x1="2048" />
            <wire x2="2224" y1="1696" y2="1696" x1="2048" />
        </branch>
        <branch name="XLXN_52">
            <wire x2="2144" y1="1440" y2="1568" x1="2144" />
            <wire x2="2224" y1="1568" y2="1568" x1="2144" />
            <wire x2="2144" y1="1568" y2="1792" x1="2144" />
            <wire x2="2144" y1="1792" y2="2016" x1="2144" />
            <wire x2="2176" y1="1792" y2="1792" x1="2144" />
            <wire x2="2224" y1="1440" y2="1440" x1="2144" />
            <wire x2="2176" y1="1056" y2="1792" x1="2176" />
            <wire x2="2224" y1="1056" y2="1056" x1="2176" />
        </branch>
        <instance x="2224" y="1952" name="XLXI_4" orien="R0" />
        <branch name="XLXN_59">
            <wire x2="736" y1="848" y2="1024" x1="736" />
            <wire x2="768" y1="1024" y2="1024" x1="736" />
            <wire x2="1760" y1="848" y2="848" x1="736" />
            <wire x2="1760" y1="848" y2="1184" x1="1760" />
            <wire x2="1760" y1="1184" y2="1184" x1="1696" />
        </branch>
        <branch name="clk">
            <wire x2="560" y1="1088" y2="1088" x1="464" />
            <wire x2="560" y1="1088" y2="1104" x1="560" />
            <wire x2="752" y1="1104" y2="1104" x1="560" />
            <wire x2="752" y1="1104" y2="1760" x1="752" />
            <wire x2="896" y1="1760" y2="1760" x1="752" />
            <wire x2="896" y1="1760" y2="1952" x1="896" />
            <wire x2="1104" y1="1760" y2="1760" x1="896" />
            <wire x2="1104" y1="1760" y2="1776" x1="1104" />
            <wire x2="1248" y1="1776" y2="1776" x1="1104" />
            <wire x2="1248" y1="1776" y2="2368" x1="1248" />
            <wire x2="1760" y1="2368" y2="2368" x1="1248" />
            <wire x2="1504" y1="1760" y2="1760" x1="1104" />
            <wire x2="768" y1="1088" y2="1088" x1="560" />
            <wire x2="1168" y1="768" y2="768" x1="560" />
            <wire x2="1168" y1="768" y2="816" x1="1168" />
            <wire x2="1168" y1="816" y2="1136" x1="1168" />
            <wire x2="1312" y1="1136" y2="1136" x1="1168" />
            <wire x2="1776" y1="816" y2="816" x1="1168" />
            <wire x2="1776" y1="816" y2="1120" x1="1776" />
            <wire x2="2032" y1="1120" y2="1120" x1="1776" />
            <wire x2="2224" y1="1120" y2="1120" x1="2032" />
            <wire x2="2032" y1="1120" y2="1632" x1="2032" />
            <wire x2="2224" y1="1632" y2="1632" x1="2032" />
            <wire x2="560" y1="768" y2="1088" x1="560" />
            <wire x2="768" y1="1952" y2="2064" x1="768" />
            <wire x2="832" y1="2064" y2="2064" x1="768" />
            <wire x2="896" y1="1952" y2="1952" x1="768" />
        </branch>
        <iomarker fontsize="28" x="464" y="1088" name="clk" orien="R180" />
        <iomarker fontsize="28" x="1296" y="896" name="rd" orien="R0" />
        <branch name="txe">
            <wire x2="768" y1="960" y2="960" x1="224" />
        </branch>
        <iomarker fontsize="28" x="224" y="960" name="txe" orien="R180" />
        <iomarker fontsize="28" x="672" y="896" name="rxf" orien="R180" />
        <branch name="rxf">
            <wire x2="768" y1="896" y2="896" x1="672" />
        </branch>
        <iomarker fontsize="28" x="224" y="1152" name="rst" orien="R180" />
        <branch name="XLXN_63">
            <wire x2="2144" y1="736" y2="992" x1="2144" />
            <wire x2="2224" y1="992" y2="992" x1="2144" />
            <wire x2="2896" y1="736" y2="736" x1="2144" />
            <wire x2="2896" y1="736" y2="1184" x1="2896" />
            <wire x2="3120" y1="1184" y2="1184" x1="2896" />
            <wire x2="3120" y1="1184" y2="1968" x1="3120" />
            <wire x2="2160" y1="1504" y2="1968" x1="2160" />
            <wire x2="3120" y1="1968" y2="1968" x1="2160" />
            <wire x2="2224" y1="1504" y2="1504" x1="2160" />
            <wire x2="3120" y1="1056" y2="1184" x1="3120" />
        </branch>
        <instance x="1760" y="2656" name="XLXI_7" orien="R0">
        </instance>
        <instance x="832" y="2352" name="XLXI_10" orien="R0">
        </instance>
        <branch name="XLXN_85">
            <wire x2="1488" y1="2064" y2="2064" x1="1216" />
            <wire x2="1488" y1="2064" y2="2432" x1="1488" />
            <wire x2="1760" y1="2432" y2="2432" x1="1488" />
        </branch>
        <branch name="XLXN_86(4:0)">
            <wire x2="1472" y1="2192" y2="2192" x1="1216" />
            <wire x2="1472" y1="2192" y2="2496" x1="1472" />
            <wire x2="1760" y1="2496" y2="2496" x1="1472" />
        </branch>
        <branch name="XLXN_87(4:0)">
            <wire x2="1456" y1="2256" y2="2256" x1="1216" />
            <wire x2="1456" y1="2256" y2="2560" x1="1456" />
            <wire x2="1760" y1="2560" y2="2560" x1="1456" />
        </branch>
        <instance x="1008" y="2672" name="XLXI_9" orien="R0">
        </instance>
        <branch name="XLXN_90">
            <wire x2="1008" y1="2512" y2="2512" x1="944" />
            <wire x2="944" y1="2512" y2="2704" x1="944" />
            <wire x2="1440" y1="2704" y2="2704" x1="944" />
            <wire x2="1440" y1="2128" y2="2128" x1="1216" />
            <wire x2="1440" y1="2128" y2="2704" x1="1440" />
        </branch>
        <branch name="XLXN_92(7:0)">
            <wire x2="800" y1="1712" y2="2640" x1="800" />
            <wire x2="1008" y1="2640" y2="2640" x1="800" />
            <wire x2="2208" y1="1712" y2="1712" x1="800" />
            <wire x2="2208" y1="1712" y2="2368" x1="2208" />
            <wire x2="2208" y1="2368" y2="2368" x1="2144" />
        </branch>
        <instance x="1504" y="1984" name="XLXI_3" orien="R0">
        </instance>
        <branch name="XLXN_30">
            <wire x2="1408" y1="1648" y2="1888" x1="1408" />
            <wire x2="1504" y1="1888" y2="1888" x1="1408" />
            <wire x2="1712" y1="1648" y2="1648" x1="1408" />
            <wire x2="1712" y1="1120" y2="1120" x1="1696" />
            <wire x2="1712" y1="1120" y2="1648" x1="1712" />
        </branch>
        <branch name="XLXN_100(7:0)">
            <wire x2="960" y1="2400" y2="2576" x1="960" />
            <wire x2="1008" y1="2576" y2="2576" x1="960" />
            <wire x2="1280" y1="2400" y2="2400" x1="960" />
            <wire x2="1280" y1="2320" y2="2320" x1="1216" />
            <wire x2="1280" y1="2320" y2="2400" x1="1280" />
        </branch>
        <branch name="leds(7:0)">
            <wire x2="1568" y1="2512" y2="2512" x1="1392" />
            <wire x2="1568" y1="2512" y2="2624" x1="1568" />
            <wire x2="1600" y1="2624" y2="2624" x1="1568" />
            <wire x2="1760" y1="2624" y2="2624" x1="1600" />
            <wire x2="1600" y1="2624" y2="2704" x1="1600" />
            <wire x2="2896" y1="2704" y2="2704" x1="1600" />
            <wire x2="2896" y1="2256" y2="2256" x1="2816" />
            <wire x2="2896" y1="2256" y2="2704" x1="2896" />
        </branch>
        <iomarker fontsize="28" x="2816" y="2256" name="leds(7:0)" orien="R180" />
        <branch name="XLXN_104(15:0)">
            <wire x2="2912" y1="1952" y2="1952" x1="1888" />
            <wire x2="2912" y1="1600" y2="1600" x1="2832" />
            <wire x2="2912" y1="1600" y2="1952" x1="2912" />
        </branch>
        <branch name="XLXN_105(15:0)">
            <wire x2="784" y1="1968" y2="2320" x1="784" />
            <wire x2="832" y1="2320" y2="2320" x1="784" />
            <wire x2="976" y1="1968" y2="1968" x1="784" />
            <wire x2="976" y1="1952" y2="1968" x1="976" />
            <wire x2="1504" y1="1952" y2="1952" x1="976" />
        </branch>
    </sheet>
</drawing>