#!/bin/perl

require("/RSCentral/Pearl-Web/library.pl") ;

&initialise_pw;

$HTMLdir        = '/export/celeb/HTML/'     ;

$DB             = 'DBI:mysql:celeb'                ;
$DBusername     = 'root'                          ;
$DBpassword     = 'RomantiC'                      ;

$DEBUGlevel     = 7                               ;

print "content-type: text/html\n\n" ;

&$sub_read_input ;
&$sub_loadFragments($HTMLdir.'main.html')              ;   #   get starting fragments
&$sub_read_input                                       ;   #   read input parameters

&$sub_write_output ;
