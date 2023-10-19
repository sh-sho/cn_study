
package me.sobata;

import io.helidon.microprofile.tests.junit5.HelidonTest;
import jakarta.inject.Inject;
import jakarta.ws.rs.client.WebTarget;
import jakarta.ws.rs.core.Response;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;

@HelidonTest
class MainTest {


    @Inject
    private WebTarget target;


    @Test
    void testMetrics() {
        Response response = target
                .path("metrics")
                .request()
                .get();
        assertThat(response.getStatus(), is(200));
    }

    @Test
    void testHealth() {
        Response response = target
                .path("health")
                .request()
                .get();
        assertThat(response.getStatus(), is(200));
    }

                
}
