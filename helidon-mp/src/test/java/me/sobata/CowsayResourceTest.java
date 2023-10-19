
package me.sobata;

import com.github.ricksbrown.cowsay.Cowsay;
import io.helidon.microprofile.tests.junit5.HelidonTest;
import jakarta.inject.Inject;
import jakarta.ws.rs.client.WebTarget;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;



@HelidonTest
@TestMethodOrder(MethodOrderer.MethodName.class)
public class CowsayResourceTest {

    private final WebTarget target;

    @Inject
    public CowsayResourceTest(WebTarget target) {
        this.target = target;
    }
    
    @Test
    public void testCowsayDefault() {
        var actual = target.path("cowsay/say").request().get(String.class);
        var expected = Cowsay.say(new String[] { "-f", "default", "Hello"});
        assertEquals(expected, actual);
    }
}
