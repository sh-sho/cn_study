
package me.opc.mp.quickstart;


import java.util.Collections;

import org.eclipse.microprofile.metrics.MetricUnits;
import org.eclipse.microprofile.metrics.annotation.Counted;
import org.eclipse.microprofile.metrics.annotation.Timed;
import jakarta.ws.rs.PathParam;

import jakarta.enterprise.context.RequestScoped;
import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
// import me.opc.mp.quickstart.Message;

import org.eclipse.microprofile.config.inject.ConfigProperty;


@Path("/cowweb/say")
public class CowsayResource {
    
    @GET
    public String getMessage(@PathParam("name") String name) {
        return String.format("Hello %s", name);
    }

}
