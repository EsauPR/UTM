--------------------------------------------------------------------------------
-- Copyright (c) 1995-2010 Xilinx, Inc.  All rights reserved.
--------------------------------------------------------------------------------
--   ____  ____ 
--  /   /\/   / 
-- /___/  \  /    Vendor: Xilinx 
-- \   \   \/     Version : 12.1
--  \   \         Application : sch2hdl
--  /   /         Filename : top.vhf
-- /___/   /\     Timestamp : 05/26/2015 21:26:44
-- \   \  /  \ 
--  \___\/\___\ 
--
--Command: sch2hdl -intstyle ise -family spartan3e -flat -suppress -vhdl C:/My_Designs/procesadorUSB/ISE/top.vhf -w C:/My_Designs/procesadorUSB/ISE/top.sch
--Design Name: top
--Device: spartan3e
--Purpose:
--    This vhdl netlist is translated from an ECS schematic. It can be 
--    synthesized and simulated, but it should not be modified. 
--

library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.ALL;
library UNISIM;
use UNISIM.Vcomponents.ALL;

entity top is
   port ( clk     : in    std_logic; 
          dataUSB : in    std_logic_vector (7 downto 0); 
          rst     : in    std_logic; 
          rxf     : in    std_logic; 
          txe     : in    std_logic; 
          leds    : out   std_logic_vector (7 downto 0); 
          rd      : out   std_logic);
end top;

architecture BEHAVIORAL of top is
   attribute INIT_00             : string ;
   attribute INIT_01             : string ;
   attribute INIT_02             : string ;
   attribute INIT_03             : string ;
   attribute INIT_04             : string ;
   attribute INIT_05             : string ;
   attribute INIT_06             : string ;
   attribute INIT_07             : string ;
   attribute INIT_08             : string ;
   attribute INIT_09             : string ;
   attribute INIT_0A             : string ;
   attribute INIT_0B             : string ;
   attribute INIT_0C             : string ;
   attribute INIT_0D             : string ;
   attribute INIT_0E             : string ;
   attribute INIT_0F             : string ;
   attribute INIT_10             : string ;
   attribute INIT_11             : string ;
   attribute INIT_12             : string ;
   attribute INIT_13             : string ;
   attribute INIT_14             : string ;
   attribute INIT_15             : string ;
   attribute INIT_16             : string ;
   attribute INIT_17             : string ;
   attribute INIT_18             : string ;
   attribute INIT_19             : string ;
   attribute INIT_1A             : string ;
   attribute INIT_1B             : string ;
   attribute INIT_1C             : string ;
   attribute INIT_1D             : string ;
   attribute INIT_1E             : string ;
   attribute INIT_1F             : string ;
   attribute INIT_20             : string ;
   attribute INIT_21             : string ;
   attribute INIT_22             : string ;
   attribute INIT_23             : string ;
   attribute INIT_24             : string ;
   attribute INIT_25             : string ;
   attribute INIT_26             : string ;
   attribute INIT_27             : string ;
   attribute INIT_28             : string ;
   attribute INIT_29             : string ;
   attribute INIT_2A             : string ;
   attribute INIT_2B             : string ;
   attribute INIT_2C             : string ;
   attribute INIT_2D             : string ;
   attribute INIT_2E             : string ;
   attribute INIT_2F             : string ;
   attribute INIT_30             : string ;
   attribute INIT_31             : string ;
   attribute INIT_32             : string ;
   attribute INIT_33             : string ;
   attribute INIT_34             : string ;
   attribute INIT_35             : string ;
   attribute INIT_36             : string ;
   attribute INIT_37             : string ;
   attribute INIT_38             : string ;
   attribute INIT_39             : string ;
   attribute INIT_3A             : string ;
   attribute INIT_3B             : string ;
   attribute INIT_3C             : string ;
   attribute INIT_3D             : string ;
   attribute INIT_3E             : string ;
   attribute INIT_3F             : string ;
   attribute INITP_00            : string ;
   attribute INITP_01            : string ;
   attribute INITP_02            : string ;
   attribute INITP_03            : string ;
   attribute INITP_04            : string ;
   attribute INITP_05            : string ;
   attribute INITP_06            : string ;
   attribute INITP_07            : string ;
   attribute SRVAL_A             : string ;
   attribute SRVAL_B             : string ;
   attribute WRITE_MODE_A        : string ;
   attribute WRITE_MODE_B        : string ;
   attribute INIT_A              : string ;
   attribute INIT_B              : string ;
   attribute SIM_COLLISION_CHECK : string ;
   attribute BOX_TYPE            : string ;
   signal XLXN_1                 : std_logic;
   signal XLXN_3                 : std_logic_vector (7 downto 0);
   signal XLXN_21                : std_logic_vector (10 downto 0);
   signal XLXN_30                : std_logic;
   signal XLXN_34                : std_logic_vector (9 downto 0);
   signal XLXN_36                : std_logic;
   signal XLXN_41                : std_logic_vector (7 downto 0);
   signal XLXN_52                : std_logic;
   signal XLXN_59                : std_logic;
   signal XLXN_63                : std_logic;
   signal XLXN_85                : std_logic;
   signal XLXN_86                : std_logic_vector (4 downto 0);
   signal XLXN_87                : std_logic_vector (4 downto 0);
   signal XLXN_90                : std_logic;
   signal XLXN_92                : std_logic_vector (7 downto 0);
   signal XLXN_100               : std_logic_vector (7 downto 0);
   signal XLXN_104               : std_logic_vector (15 downto 0);
   signal XLXN_105               : std_logic_vector (15 downto 0);
   signal leds_DUMMY             : std_logic_vector (7 downto 0);
   signal XLXI_4_DIB_openSignal  : std_logic_vector (15 downto 0);
   signal XLXI_4_DIPA_openSignal : std_logic_vector (0 downto 0);
   signal XLXI_4_DIPB_openSignal : std_logic_vector (1 downto 0);
   component uart
      port ( rxf     : in    std_logic; 
             txe     : in    std_logic; 
             rd_u    : in    std_logic; 
             clk     : in    std_logic; 
             rst     : in    std_logic; 
             dataUSB : in    std_logic_vector (7 downto 0); 
             rd      : out   std_logic; 
             da      : out   std_logic; 
             dato    : out   std_logic_vector (7 downto 0));
   end component;
   
   component ucp
      port ( DA     : in    std_logic; 
             clk    : in    std_logic; 
             rst    : in    std_logic; 
             datoRX : in    std_logic_vector (7 downto 0); 
             WR     : out   std_logic; 
             P_OK   : out   std_logic; 
             RD     : out   std_logic; 
             dato   : out   std_logic_vector (7 downto 0); 
             dir    : out   std_logic_vector (10 downto 0));
   end component;
   
   component UC
      port ( clk  : in    std_logic; 
             rst  : in    std_logic; 
             P_OK : in    std_logic; 
             IR   : in    std_logic_vector (15 downto 0); 
             dato : out   std_logic_vector (15 downto 0); 
             PC   : out   std_logic_vector (9 downto 0));
   end component;
   
   component RAMB16_S9_S18
      -- synopsys translate_off
      generic( INIT_00 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_01 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_02 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_03 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_04 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_05 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_06 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_07 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_08 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_09 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0A : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0B : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0C : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0D : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0E : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_0F : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_10 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_11 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_12 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_13 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_14 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_15 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_16 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_17 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_18 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_19 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1A : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1B : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1C : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1D : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1E : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_1F : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_20 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_21 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_22 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_23 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_24 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_25 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_26 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_27 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_28 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_29 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2A : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2B : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2C : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2D : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2E : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_2F : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_30 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_31 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_32 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_33 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_34 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_35 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_36 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_37 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_38 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_39 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3A : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3B : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3C : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3D : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3E : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INIT_3F : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_00 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_01 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_02 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_03 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_04 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_05 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_06 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               INITP_07 : bit_vector :=  
            x"0000000000000000000000000000000000000000000000000000000000000000";
               SRVAL_A : bit_vector :=  x"000";
               SRVAL_B : bit_vector :=  x"00000";
               WRITE_MODE_A : string :=  "WRITE_FIRST";
               WRITE_MODE_B : string :=  "WRITE_FIRST";
               INIT_A : bit_vector :=  x"000";
               INIT_B : bit_vector :=  x"00000";
               SIM_COLLISION_CHECK : string :=  "ALL");
      -- synopsys translate_on
      port ( ADDRA : in    std_logic_vector (10 downto 0); 
             ADDRB : in    std_logic_vector (9 downto 0); 
             CLKA  : in    std_logic; 
             CLKB  : in    std_logic; 
             DIA   : in    std_logic_vector (7 downto 0); 
             DIB   : in    std_logic_vector (15 downto 0); 
             DIPA  : in    std_logic_vector (0 downto 0); 
             DIPB  : in    std_logic_vector (1 downto 0); 
             ENA   : in    std_logic; 
             ENB   : in    std_logic; 
             SSRA  : in    std_logic; 
             SSRB  : in    std_logic; 
             WEA   : in    std_logic; 
             WEB   : in    std_logic; 
             DOA   : out   std_logic_vector (7 downto 0); 
             DOB   : out   std_logic_vector (15 downto 0); 
             DOPA  : out   std_logic_vector (0 downto 0); 
             DOPB  : out   std_logic_vector (1 downto 0));
   end component;
   attribute INIT_00 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_01 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_02 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_03 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_04 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_05 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_06 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_07 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_08 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_09 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0A of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0B of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0C of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0D of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0E of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_0F of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_10 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_11 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_12 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_13 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_14 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_15 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_16 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_17 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_18 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_19 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1A of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1B of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1C of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1D of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1E of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_1F of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_20 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_21 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_22 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_23 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_24 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_25 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_26 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_27 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_28 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_29 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2A of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2B of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2C of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2D of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2E of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_2F of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_30 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_31 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_32 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_33 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_34 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_35 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_36 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_37 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_38 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_39 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3A of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3B of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3C of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3D of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3E of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INIT_3F of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_00 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_01 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_02 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_03 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_04 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_05 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_06 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute INITP_07 of RAMB16_S9_S18 : component is 
         "0000000000000000000000000000000000000000000000000000000000000000";
   attribute SRVAL_A of RAMB16_S9_S18 : component is "000";
   attribute SRVAL_B of RAMB16_S9_S18 : component is "00000";
   attribute WRITE_MODE_A of RAMB16_S9_S18 : component is "WRITE_FIRST";
   attribute WRITE_MODE_B of RAMB16_S9_S18 : component is "WRITE_FIRST";
   attribute INIT_A of RAMB16_S9_S18 : component is "000";
   attribute INIT_B of RAMB16_S9_S18 : component is "00000";
   attribute SIM_COLLISION_CHECK of RAMB16_S9_S18 : component is "ALL";
   attribute BOX_TYPE of RAMB16_S9_S18 : component is "BLACK_BOX";
   
   component GND
      port ( G : out   std_logic);
   end component;
   attribute BOX_TYPE of GND : component is "BLACK_BOX";
   
   component VCC
      port ( P : out   std_logic);
   end component;
   attribute BOX_TYPE of VCC : component is "BLACK_BOX";
   
   component AR
      port ( clk    : in    std_logic; 
             ctr    : in    std_logic; 
             AddrRd : in    std_logic_vector (4 downto 0); 
             AddrRr : in    std_logic_vector (4 downto 0); 
             DataIn : in    std_logic_vector (7 downto 0); 
             Rr     : out   std_logic_vector (7 downto 0); 
             Rd     : out   std_logic_vector (7 downto 0));
   end component;
   
   component MUX
      port ( sel    : in    std_logic; 
             D1     : in    std_logic_vector (7 downto 0); 
             D0     : in    std_logic_vector (7 downto 0); 
             SALIDA : out   std_logic_vector (7 downto 0));
   end component;
   
   component PU
      port ( clk       : in    std_logic; 
             CO        : in    std_logic_vector (15 downto 0); 
             wr        : out   std_logic; 
             sel       : out   std_logic; 
             AddrRd    : out   std_logic_vector (4 downto 0); 
             AddrRr    : out   std_logic_vector (4 downto 0); 
             constante : out   std_logic_vector (7 downto 0));
   end component;
   
   attribute INIT_00 of XLXI_4 : label is 
         "0000000000000000000000000000000000000000000000000000000000111111";
   attribute INIT_01 of XLXI_4 : label is 
         "0200020002000200020002000200020002000200020002000200020002000200";
   attribute INIT_02 of XLXI_4 : label is 
         "0300030003000300030003000300030003000300030003000300030003000300";
begin
   leds(7 downto 0) <= leds_DUMMY(7 downto 0);
   XLXI_1 : uart
      port map (clk=>clk,
                dataUSB(7 downto 0)=>dataUSB(7 downto 0),
                rd_u=>XLXN_59,
                rst=>rst,
                rxf=>rxf,
                txe=>txe,
                da=>XLXN_1,
                dato(7 downto 0)=>XLXN_3(7 downto 0),
                rd=>rd);
   
   XLXI_2 : ucp
      port map (clk=>clk,
                DA=>XLXN_1,
                datoRX(7 downto 0)=>XLXN_3(7 downto 0),
                rst=>rst,
                dato(7 downto 0)=>XLXN_41(7 downto 0),
                dir(10 downto 0)=>XLXN_21(10 downto 0),
                P_OK=>XLXN_30,
                RD=>XLXN_59,
                WR=>XLXN_36);
   
   XLXI_3 : UC
      port map (clk=>clk,
                IR(15 downto 0)=>XLXN_104(15 downto 0),
                P_OK=>XLXN_30,
                rst=>rst,
                dato(15 downto 0)=>XLXN_105(15 downto 0),
                PC(9 downto 0)=>XLXN_34(9 downto 0));
   
   XLXI_4 : RAMB16_S9_S18
   -- synopsys translate_off
   generic map( INIT_00 => 
         x"0000000000000000000000000000000000000000000000000000000000111111",
            INIT_01 => 
         x"0200020002000200020002000200020002000200020002000200020002000200",
            INIT_02 => 
         x"0300030003000300030003000300030003000300030003000300030003000300")
   -- synopsys translate_on
      port map (ADDRA(10 downto 0)=>XLXN_21(10 downto 0),
                ADDRB(9 downto 0)=>XLXN_34(9 downto 0),
                CLKA=>clk,
                CLKB=>clk,
                DIA(7 downto 0)=>XLXN_41(7 downto 0),
                DIB(15 downto 0)=>XLXI_4_DIB_openSignal(15 downto 0),
                DIPA(0)=>XLXI_4_DIPA_openSignal(0),
                DIPB(1 downto 0)=>XLXI_4_DIPB_openSignal(1 downto 0),
                ENA=>XLXN_63,
                ENB=>XLXN_63,
                SSRA=>XLXN_52,
                SSRB=>XLXN_52,
                WEA=>XLXN_36,
                WEB=>XLXN_52,
                DOA=>open,
                DOB(15 downto 0)=>XLXN_104(15 downto 0),
                DOPA=>open,
                DOPB=>open);
   
   XLXI_5 : GND
      port map (G=>XLXN_52);
   
   XLXI_6 : VCC
      port map (P=>XLXN_63);
   
   XLXI_7 : AR
      port map (AddrRd(4 downto 0)=>XLXN_86(4 downto 0),
                AddrRr(4 downto 0)=>XLXN_87(4 downto 0),
                clk=>clk,
                ctr=>XLXN_85,
                DataIn(7 downto 0)=>leds_DUMMY(7 downto 0),
                Rd=>open,
                Rr(7 downto 0)=>XLXN_92(7 downto 0));
   
   XLXI_9 : MUX
      port map (D0(7 downto 0)=>XLXN_92(7 downto 0),
                D1(7 downto 0)=>XLXN_100(7 downto 0),
                sel=>XLXN_90,
                SALIDA(7 downto 0)=>leds_DUMMY(7 downto 0));
   
   XLXI_10 : PU
      port map (clk=>clk,
                CO(15 downto 0)=>XLXN_105(15 downto 0),
                AddrRd(4 downto 0)=>XLXN_86(4 downto 0),
                AddrRr(4 downto 0)=>XLXN_87(4 downto 0),
                constante(7 downto 0)=>XLXN_100(7 downto 0),
                sel=>XLXN_90,
                wr=>XLXN_85);
   
end BEHAVIORAL;


