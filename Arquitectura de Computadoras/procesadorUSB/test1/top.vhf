--------------------------------------------------------------------------------
-- Copyright (c) 1995-2010 Xilinx, Inc.  All rights reserved.
--------------------------------------------------------------------------------
--   ____  ____ 
--  /   /\/   / 
-- /___/  \  /    Vendor: Xilinx 
-- \   \   \/     Version : 12.1
--  \   \         Application : sch2hdl
--  /   /         Filename : top.vhf
-- /___/   /\     Timestamp : 05/12/2015 20:47:36
-- \   \  /  \ 
--  \___\/\___\ 
--
--Command: sch2hdl -intstyle ise -family spartan3e -flat -suppress -vhdl C:/My_Designs/procesadorUSB/test1/top.vhf -w C:/My_Designs/procesadorUSB/test1/top.sch
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
   signal XLXN_1  : std_logic;
   signal XLXN_2  : std_logic;
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
   
   component desplegador
      port ( da   : in    std_logic; 
             clk  : in    std_logic; 
             rd_u : out   std_logic);
   end component;
   
begin
   XLXI_1 : uart
      port map (clk=>clk,
                dataUSB(7 downto 0)=>dataUSB(7 downto 0),
                rd_u=>XLXN_2,
                rst=>rst,
                rxf=>rxf,
                txe=>txe,
                da=>XLXN_1,
                dato(7 downto 0)=>leds(7 downto 0),
                rd=>rd);
   
   XLXI_2 : desplegador
      port map (clk=>clk,
                da=>XLXN_1,
                rd_u=>XLXN_2);
   
end BEHAVIORAL;


