<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="spartan3e" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="clk" />
        <signal name="rst" />
        <signal name="btn" />
        <signal name="rxf" />
        <signal name="txe" />
        <signal name="dataUSB(7:0)" />
        <signal name="da" />
        <signal name="rd" />
        <signal name="XLXN_12(7:0)" />
        <signal name="XLXN_13" />
        <signal name="XLXN_14" />
        <signal name="XLXN_15" />
        <signal name="XLXN_19" />
        <signal name="XLXN_20" />
        <signal name="XLXN_21(7:0)" />
        <signal name="XLXN_22(10:0)" />
        <signal name="XLXN_24(15:0)" />
        <signal name="XLXN_26(9:0)" />
        <signal name="leds(7:0)" />
        <port polarity="Input" name="clk" />
        <port polarity="Input" name="rst" />
        <port polarity="Input" name="btn" />
        <port polarity="Input" name="rxf" />
        <port polarity="Input" name="txe" />
        <port polarity="Input" name="dataUSB(7:0)" />
        <port polarity="Output" name="rd" />
        <port polarity="Output" name="leds(7:0)" />
        <blockdef name="UC">
            <timestamp>2015-5-9T2:6:4</timestamp>
            <rect width="64" x="0" y="84" height="24" />
            <line x2="0" y1="96" y2="96" x1="64" />
            <rect width="64" x="320" y="84" height="24" />
            <line x2="384" y1="96" y2="96" x1="320" />
            <line x2="0" y1="32" y2="32" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <rect width="64" x="320" y="-172" height="24" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <rect width="256" x="64" y="-192" height="320" />
        </blockdef>
        <blockdef name="uart">
            <timestamp>2015-5-9T1:23:8</timestamp>
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
            <timestamp>2015-5-9T1:9:29</timestamp>
            <rect width="256" x="64" y="-320" height="320" />
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-208" y2="-208" x1="64" />
            <line x2="0" y1="-128" y2="-128" x1="64" />
            <rect width="64" x="0" y="-60" height="24" />
            <line x2="0" y1="-48" y2="-48" x1="64" />
            <line x2="384" y1="-288" y2="-288" x1="320" />
            <line x2="384" y1="-224" y2="-224" x1="320" />
            <line x2="384" y1="-160" y2="-160" x1="320" />
            <rect width="64" x="320" y="-108" height="24" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
            <rect width="64" x="320" y="-44" height="24" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
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
        <block symbolname="UC" name="XLXI_1">
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="XLXN_14" name="P_OK" />
            <blockpin signalname="btn" name="btn" />
            <blockpin signalname="XLXN_24(15:0)" name="IR(15:0)" />
            <blockpin signalname="leds(7:0)" name="dato(7:0)" />
            <blockpin signalname="XLXN_26(9:0)" name="PC(9:0)" />
        </block>
        <block symbolname="uart" name="XLXI_2">
            <blockpin signalname="rxf" name="rxf" />
            <blockpin signalname="txe" name="txe" />
            <blockpin signalname="XLXN_13" name="rd_u" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="dataUSB(7:0)" name="dataUSB(7:0)" />
            <blockpin signalname="rd" name="rd" />
            <blockpin signalname="da" name="da" />
            <blockpin signalname="XLXN_12(7:0)" name="dato(7:0)" />
        </block>
        <block symbolname="ucp" name="XLXI_3">
            <blockpin signalname="da" name="DA" />
            <blockpin signalname="clk" name="clk" />
            <blockpin signalname="rst" name="rst" />
            <blockpin signalname="XLXN_12(7:0)" name="datoRX(7:0)" />
            <blockpin signalname="XLXN_20" name="WR" />
            <blockpin signalname="XLXN_14" name="P_OK" />
            <blockpin signalname="XLXN_13" name="RD" />
            <blockpin signalname="XLXN_21(7:0)" name="dato(7:0)" />
            <blockpin signalname="XLXN_22(10:0)" name="dir(10:0)" />
        </block>
        <block symbolname="ramb16_s9_s18" name="XLXI_4">
            <attr value="111111111111111111111111111111111111111111111111111111111111111" name="INIT_00">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="111111111111111111111111111111111111111111111111111111111111111" name="INITP_06">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="111111111111111111111111111111111111111111111111111111111111111" name="INITP_04">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="111111111111111111111111111111111111111111111111111111111111111" name="INITP_02">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <attr value="111111111111111111111111111111111111111111111111111111111111111" name="INITP_00">
                <trait verilog="all:0 dp:1nosynth wsynop:1 wsynth:1" />
                <trait vhdl="all:0 gm:1nosynth wa:1 wd:1" />
                <trait valuetype="BitVector 256 h" />
            </attr>
            <blockpin signalname="XLXN_22(10:0)" name="ADDRA(10:0)" />
            <blockpin signalname="XLXN_26(9:0)" name="ADDRB(9:0)" />
            <blockpin signalname="clk" name="CLKA" />
            <blockpin signalname="clk" name="CLKB" />
            <blockpin signalname="XLXN_21(7:0)" name="DIA(7:0)" />
            <blockpin name="DIB(15:0)" />
            <blockpin name="DIPA(0:0)" />
            <blockpin name="DIPB(1:0)" />
            <blockpin signalname="XLXN_19" name="ENA" />
            <blockpin signalname="XLXN_19" name="ENB" />
            <blockpin signalname="XLXN_15" name="SSRA" />
            <blockpin signalname="XLXN_15" name="SSRB" />
            <blockpin signalname="XLXN_20" name="WEA" />
            <blockpin signalname="XLXN_15" name="WEB" />
            <blockpin name="DOA(7:0)" />
            <blockpin signalname="XLXN_24(15:0)" name="DOB(15:0)" />
            <blockpin name="DOPA(0:0)" />
            <blockpin name="DOPB(1:0)" />
        </block>
        <block symbolname="gnd" name="XLXI_5">
            <blockpin signalname="XLXN_15" name="G" />
        </block>
        <block symbolname="vcc" name="XLXI_6">
            <blockpin signalname="XLXN_19" name="P" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <branch name="clk">
            <wire x2="672" y1="992" y2="992" x1="512" />
            <wire x2="672" y1="992" y2="1536" x1="672" />
            <wire x2="672" y1="1536" y2="1552" x1="672" />
            <wire x2="1312" y1="1552" y2="1552" x1="672" />
            <wire x2="672" y1="640" y2="640" x1="656" />
            <wire x2="656" y1="640" y2="864" x1="656" />
            <wire x2="672" y1="864" y2="864" x1="656" />
            <wire x2="672" y1="864" y2="992" x1="672" />
            <wire x2="1104" y1="864" y2="864" x1="672" />
            <wire x2="656" y1="1472" y2="1536" x1="656" />
            <wire x2="672" y1="1536" y2="1536" x1="656" />
            <wire x2="1456" y1="1472" y2="1472" x1="656" />
            <wire x2="1504" y1="592" y2="592" x1="1104" />
            <wire x2="1104" y1="592" y2="608" x1="1104" />
            <wire x2="1104" y1="608" y2="864" x1="1104" />
            <wire x2="1136" y1="608" y2="608" x1="1104" />
            <wire x2="1136" y1="608" y2="864" x1="1136" />
            <wire x2="2016" y1="864" y2="864" x1="1136" />
            <wire x2="1456" y1="1152" y2="1472" x1="1456" />
            <wire x2="2736" y1="1152" y2="1152" x1="1456" />
            <wire x2="2016" y1="640" y2="864" x1="2016" />
            <wire x2="2736" y1="640" y2="640" x1="2016" />
        </branch>
        <branch name="rst">
            <wire x2="336" y1="704" y2="1136" x1="336" />
            <wire x2="608" y1="1136" y2="1136" x1="336" />
            <wire x2="672" y1="704" y2="704" x1="336" />
            <wire x2="608" y1="1056" y2="1056" x1="512" />
            <wire x2="608" y1="1056" y2="1136" x1="608" />
            <wire x2="960" y1="1056" y2="1056" x1="608" />
            <wire x2="960" y1="1056" y2="1616" x1="960" />
            <wire x2="1312" y1="1616" y2="1616" x1="960" />
            <wire x2="1232" y1="1056" y2="1056" x1="960" />
            <wire x2="1232" y1="672" y2="1056" x1="1232" />
            <wire x2="1504" y1="672" y2="672" x1="1232" />
        </branch>
        <branch name="btn">
            <wire x2="1264" y1="1456" y2="1680" x1="1264" />
            <wire x2="1312" y1="1680" y2="1680" x1="1264" />
            <wire x2="1392" y1="1456" y2="1456" x1="1264" />
            <wire x2="1392" y1="1120" y2="1120" x1="1376" />
            <wire x2="1392" y1="1120" y2="1456" x1="1392" />
        </branch>
        <iomarker fontsize="28" x="1376" y="1120" name="btn" orien="R180" />
        <instance x="672" y="800" name="XLXI_2" orien="R0">
        </instance>
        <branch name="rxf">
            <wire x2="672" y1="448" y2="448" x1="640" />
        </branch>
        <iomarker fontsize="28" x="640" y="448" name="rxf" orien="R180" />
        <branch name="txe">
            <wire x2="672" y1="512" y2="512" x1="640" />
        </branch>
        <iomarker fontsize="28" x="640" y="512" name="txe" orien="R180" />
        <branch name="dataUSB(7:0)">
            <wire x2="672" y1="768" y2="768" x1="640" />
        </branch>
        <iomarker fontsize="28" x="640" y="768" name="dataUSB(7:0)" orien="R180" />
        <branch name="da">
            <attrtext style="alignment:SOFT-TCENTER" attrname="Name" x="1088" y="608" type="branch" />
            <wire x2="1088" y1="608" y2="608" x1="1056" />
            <wire x2="1504" y1="512" y2="512" x1="1088" />
            <wire x2="1088" y1="512" y2="608" x1="1088" />
        </branch>
        <iomarker fontsize="28" x="512" y="992" name="clk" orien="R180" />
        <iomarker fontsize="28" x="512" y="1056" name="rst" orien="R180" />
        <branch name="rd">
            <wire x2="1088" y1="448" y2="448" x1="1056" />
        </branch>
        <iomarker fontsize="28" x="1088" y="448" name="rd" orien="R0" />
        <instance x="1312" y="1712" name="XLXI_1" orien="R0">
        </instance>
        <instance x="1504" y="800" name="XLXI_3" orien="R0">
        </instance>
        <branch name="XLXN_12(7:0)">
            <wire x2="1280" y1="768" y2="768" x1="1056" />
            <wire x2="1280" y1="752" y2="768" x1="1280" />
            <wire x2="1504" y1="752" y2="752" x1="1280" />
        </branch>
        <branch name="XLXN_13">
            <wire x2="464" y1="352" y2="576" x1="464" />
            <wire x2="672" y1="576" y2="576" x1="464" />
            <wire x2="1952" y1="352" y2="352" x1="464" />
            <wire x2="1952" y1="352" y2="640" x1="1952" />
            <wire x2="1952" y1="640" y2="640" x1="1888" />
        </branch>
        <branch name="XLXN_14">
            <wire x2="1312" y1="1744" y2="1744" x1="1248" />
            <wire x2="1248" y1="1744" y2="1840" x1="1248" />
            <wire x2="2048" y1="1840" y2="1840" x1="1248" />
            <wire x2="2048" y1="576" y2="576" x1="1888" />
            <wire x2="2048" y1="576" y2="1840" x1="2048" />
        </branch>
        <iomarker fontsize="28" x="1808" y="1552" name="leds(7:0)" orien="R0" />
        <instance x="2736" y="1472" name="XLXI_4" orien="R0" />
        <instance x="2448" y="1056" name="XLXI_5" orien="R0" />
        <instance x="2448" y="784" name="XLXI_6" orien="R0" />
        <branch name="XLXN_15">
            <wire x2="2512" y1="864" y2="928" x1="2512" />
            <wire x2="2608" y1="864" y2="864" x1="2512" />
            <wire x2="2608" y1="864" y2="960" x1="2608" />
            <wire x2="2736" y1="960" y2="960" x1="2608" />
            <wire x2="2608" y1="960" y2="1088" x1="2608" />
            <wire x2="2736" y1="1088" y2="1088" x1="2608" />
            <wire x2="2608" y1="576" y2="864" x1="2608" />
            <wire x2="2736" y1="576" y2="576" x1="2608" />
        </branch>
        <branch name="XLXN_19">
            <wire x2="2432" y1="512" y2="848" x1="2432" />
            <wire x2="2512" y1="848" y2="848" x1="2432" />
            <wire x2="2432" y1="848" y2="912" x1="2432" />
            <wire x2="2592" y1="912" y2="912" x1="2432" />
            <wire x2="2592" y1="912" y2="1024" x1="2592" />
            <wire x2="2736" y1="1024" y2="1024" x1="2592" />
            <wire x2="2736" y1="512" y2="512" x1="2432" />
            <wire x2="2512" y1="784" y2="848" x1="2512" />
        </branch>
        <branch name="XLXN_20">
            <wire x2="2304" y1="512" y2="512" x1="1888" />
            <wire x2="2304" y1="448" y2="512" x1="2304" />
            <wire x2="2736" y1="448" y2="448" x1="2304" />
        </branch>
        <branch name="XLXN_21(7:0)">
            <wire x2="2592" y1="704" y2="704" x1="1888" />
            <wire x2="2592" y1="704" y2="768" x1="2592" />
            <wire x2="2736" y1="768" y2="768" x1="2592" />
        </branch>
        <branch name="XLXN_22(10:0)">
            <wire x2="1952" y1="768" y2="768" x1="1888" />
            <wire x2="1952" y1="768" y2="800" x1="1952" />
            <wire x2="2640" y1="800" y2="800" x1="1952" />
            <wire x2="2640" y1="704" y2="800" x1="2640" />
            <wire x2="2736" y1="704" y2="704" x1="2640" />
        </branch>
        <branch name="XLXN_24(15:0)">
            <wire x2="1312" y1="1808" y2="1808" x1="1264" />
            <wire x2="1264" y1="1808" y2="1904" x1="1264" />
            <wire x2="3424" y1="1904" y2="1904" x1="1264" />
            <wire x2="3424" y1="1120" y2="1120" x1="3344" />
            <wire x2="3424" y1="1120" y2="1904" x1="3424" />
        </branch>
        <branch name="XLXN_26(9:0)">
            <wire x2="2208" y1="1808" y2="1808" x1="1696" />
            <wire x2="2208" y1="1216" y2="1808" x1="2208" />
            <wire x2="2736" y1="1216" y2="1216" x1="2208" />
        </branch>
        <branch name="leds(7:0)">
            <wire x2="1808" y1="1552" y2="1552" x1="1696" />
        </branch>
    </sheet>
</drawing>