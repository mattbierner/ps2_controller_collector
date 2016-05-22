/**
 * Simple logger for PlayStation 2 controller state using SPI.
 */
#include <SPI.h>

#define DEBUG 0

// State
byte buf [100];
volatile byte pos;
volatile byte process;

#if DEBUG
void printHex(byte b) {
  char tmp[16];

  sprintf(tmp, "%02x", b);
  Serial.print(tmp);
}

void printBits(byte b) {
  for (int i = 7; i >= 0; --i)
    Serial.print((b >> i) & 1);
}
#endif

void setup (void) {
  Serial.begin (115200);

  // Configure SPI as slave
  SPCR |= bit (SPE);
  SPCR |= bit (CPOL);
  SPCR |= bit (CPHA);
  SPCR |= bit (DORD);

  pos = 0;
  process = false;
  
  // Turn on interrupts
  SPI.attachInterrupt();
}

/**
 * SPI interrupt
 */
ISR (SPI_STC_vect) {
  byte c = SPDR;
  if (pos < sizeof buf) {
    buf[pos++] = c;
  }
  process = true;
}

void loop (void) {
  if (process && pos >= 8) {
    // probs could be done on computer instead of here but whatev
    if (buf[1] == 0x73) {
      Serial.print(buf[3], DEC);
      Serial.print(", ");
      Serial.print(buf[4], DEC);
      Serial.print(", ");
      Serial.print(buf[5], DEC);
      Serial.print(", ");
      Serial.print(buf[6], DEC);
      Serial.print(", ");
      Serial.print(buf[7], DEC);
      Serial.print(", ");
      Serial.print(buf[8], DEC);
      Serial.print("\n");
    }

#if DEBUG
    for (unsigned i = 0; i < pos; ++i) {
      //printHex(buf[i]);
      printBits(buf[i]);
      Serial.print(':');
    }
    Serial.print("\n");
#endif
    
    pos = 0;
    process = false;
  }
}
